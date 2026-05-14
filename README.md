# cirrus-cloudflare-agent

> A full-stack AI agent built entirely on Cloudflare — no traditional hosting, just a domain.

🌐 **Live demo**: [focuseffect.fr](https://focuseffect.fr)  
🔒 **Mission Control** (internal): [focuseffect.fr/#csm-cirrus-internal](https://focuseffect.fr/#csm-cirrus-internal)

---

## What is this?

**Cirrus** is an AI-powered web agent that runs 100% on Cloudflare's edge infrastructure. No servers. No traditional hosting. No cloud VMs. Just a domain name and Cloudflare.

It demonstrates that you can build a complete, production-grade application — with persistent memory, real-time AI responses, live data feeds, and a dynamic frontend — using only Cloudflare products.

Cirrus is also a multilingual Cloudflare expert that speaks EN, FR, ES, PT, ZH (中文), and JA (日本語). It knows every product, every use case, and every reason your infrastructure could be faster, safer, and smarter.

---

## Cloudflare Products — Actively Deployed

| Product | Role | Config |
|---|---|---|
| **Cloudflare Pages** | Frontend hosting at the edge. Static site globally distributed. CI/CD via Wrangler CLI. Custom domain auto-configured. | Free tier |
| **Cloudflare Workers** | The entire Cirrus backend. `POST /` handles AI chat. `GET /` serves live RSS news as structured JSON. | Paid |
| **Workers AI** | LLM inference at the edge. No GPU provisioning required. | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` · 2048 max tokens |
| **AI Gateway** | All Workers AI requests routed through it. Handles caching, request logging, and cost monitoring. | id: `default` · Cache TTL: 3600s |
| **Workers KV** | Persistent cross-session conversation memory per user (UUID-keyed). | Binding: `CACHE` · TTL: 7 days · Stores last 3 turns as JSON |
| **Cloudflare DNS** | Custom domain routing. CNAME auto-created when adding domain in Pages dashboard. | Free |

---

## Cloudflare Products — In the AI Knowledge Base

Cirrus's system prompt contains deep technical knowledge of the full Cloudflare stack. These products are actively recommended, explained, and compared during conversations, audits, and calculator sessions.

### AI Platform

| Product | Role |
|---|---|
| **Workers AI** | Edge inference. 50+ models. Pay only for CPU time (not wall time) — critical for agentic workloads. |
| **AI Gateway** | Universal proxy for any AI provider (OpenAI, Anthropic, Workers AI). Caching, logging, rate limiting, fallback. |
| **AI Search (Beta)** | Managed RAG-as-a-service. Connect a website or R2 bucket → semantic search with no infrastructure. Integrates natively with Vectorize, R2, AI Gateway, Browser Rendering. |
| **Vectorize** | Vector database for semantic search and RAG pipelines. Integrates with Workers AI and AI Search. |
| **Agents SDK** | Build autonomous AI agents with memory, tool calling, scheduling. Built on Durable Objects + Workers. WebSocket hibernation = zero cost when idle. |
| **AutoRAG** | Automatic RAG pipelines from R2 documents. |
| **Browser Rendering** | Headless browser for AI agents to interact with websites. |
| **MCP Servers** | Model Context Protocol — connect agents to any external API, hosted on Workers. |
| **Workflows** | Durable multi-step AI pipelines with automatic retry per step. |
| **Durable Objects** | Stateful serverless — backbone of the Agents SDK. |

### Security

| Product | Role |
|---|---|
| **DDoS Protection** | Unmetered, automatic, always-on. 321 Tbps+ network capacity. |
| **WAF** | Web Application Firewall. Managed rules (Pro), custom rules (Business), unlimited (Enterprise). |
| **Bot Management** | ML-based bot detection. Stops credential stuffing, scraping, fake traffic. |
| **Page Shield** | Detects malicious JS injected via third-party scripts (supply chain attacks). |
| **Zero Trust / SASE** | Cloudflare Access + Tunnel + WARP. Replaces VPN. Free up to 50 users. |
| **Magic Transit** | Network-layer DDoS protection for enterprise IP infrastructure. |
| **Email Security** | Anti-phishing and malware protection. |
| **Turnstile** | Privacy-first CAPTCHA alternative. No user tracking. |
| **Rate Limiting** | API and login page protection. |
| **API Shield** | Automatic API discovery, schema validation, and protection. |
| **Agile SASE Platform** | Unified network security and connectivity. |

### Performance & Developer Platform

| Product | Role |
|---|---|
| **CDN** | 330+ datacenters, sub-10ms DNS, automatic caching. |
| **Argo Smart Routing** | Intelligent routing avoiding congested internet paths. ~30% latency reduction. |
| **Image Optimization** | Polish + Mirage. Auto-compress, resize, WebP conversion. |
| **Load Balancing** | Traffic distribution with real-time health checks. |
| **Waiting Room** | Virtual queue for traffic spikes. |
| **R2** | S3-compatible object storage. Zero egress fees. |
| **D1** | Serverless SQLite at the edge. |
| **KV** | Global key-value store. Ultra-fast reads everywhere. |
| **Queues** | Async message queue for background processing. |
| **Hyperdrive** | Connection pooling for Workers → existing Postgres/MySQL databases. |
| **Web3** | IPFS and Ethereum gateways at the edge. |

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        User Browser                          │
│      localStorage: userId · userName · chatHistory           │
└─────────────────────────┬────────────────────────────────────┘
                          │ HTTPS
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                   Cloudflare DNS                             │
│   focuseffect.fr → CNAME → focuseffect-site.pages.dev        │
│   (auto-created by Pages when adding custom domain)          │
└─────────────────────────┬────────────────────────────────────┘
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                   Cloudflare Pages                           │
│     Edge-served HTML/CSS/JS · 330+ datacenters worldwide     │
│     Generated by write_site.py · Deployed via Wrangler CLI   │
│                                                              │
│  ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌─────────────┐  │
│  │  Ask     │ │ Products │ │ Calculator │ │    Audit    │  │
│  │ Cirrus   │ │ Catalog  │ │  + AI opps │ │    News     │  │
│  └──────────┘ └──────────┘ └────────────┘ └─────────────┘  │
│              + Mission Control (hidden · #csm-cirrus-internal)│
└─────────────────────────┬────────────────────────────────────┘
                          │ fetch()
          ┌───────────────┴────────────────┐
          │ POST / (chat)                  │ GET / (news)
          ▼                                ▼
┌──────────────────────────────────────────────────────────────┐
│                   Cloudflare Worker                          │
│                                                              │
│  POST / (chat)                      GET / (news)             │
│  ├─ Read KV memory (userId)         ├─ Fetch CF Blog RSS     │
│  ├─ Build dynamic system prompt     ├─ Fetch CF Changelog RSS│
│  │   · Full product knowledge base  └─ Return structured JSON│
│  │   · Live UTC timestamp                (title, date, desc, │
│  │   · userName + detected language       source, link)      │
│  ├─ Route through AI Gateway                                 │
│  ├─ Call Workers AI (LLM)                                    │
│  └─ Write updated history to KV                              │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                    AI Gateway                          │  │
│  │  id: "default" · Cache TTL: 3600s                      │  │
│  │  Logs every request · Monitors cost · Caches responses │  │
│  └───────────────────────┬────────────────────────────────┘  │
│                          ▼                                   │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                    Workers AI                          │  │
│  │  @cf/meta/llama-3.3-70b-instruct-fp8-fast              │  │
│  │  System prompt: product catalog + UTC time + userName  │  │
│  │  Conversation history: last 3 turns from KV            │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐  │
│  │                    Workers KV                          │  │
│  │  Binding: CACHE · Key: "conv_" + userId                │  │
│  │  Value: JSON array of last 3 message pairs             │  │
│  │  TTL: 7 days · Cross-session persistent memory         │  │
│  └────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## Features

### Ask Cirrus (AI Agent)
- Conversational AI with cross-session memory (localStorage + Workers KV)
- Language auto-detection — responds exclusively in the user's language
- First name detection via regex → stored in localStorage → passed to Worker → used in KV context
- 5 rotating welcome messages per new conversation
- Full markdown rendering: `**bold**`, `####` headers in orange, bullet points, line breaks
- Em-dash (`—`) auto-replaced in `formatMarkdown()` to avoid rendering artifacts
- General conversation enabled — Cirrus is not limited to Cloudflare topics
- Current UTC datetime injected dynamically into every system prompt
- "Clear chat" button resets localStorage and KV context

### Cirrus (Manga-Cyborg Mascot)
- SVG character: large purple manga eyes, orange hair streaks, square cyber jacket, orange boots, right-side cyborg plate
- Orange glow: `drop-shadow(0 0 6px rgba(249,115,22,0.8)) drop-shadow(0 0 14px rgba(249,115,22,0.35))`
- Float animation: `translateY(-7px)` ease-in-out loop, 3.5s
- Left of the chat box on Ask Cirrus section with speech bubble
- Fixed bottom-right corner on all other sections with contextual bubbles per section
- Clicking anywhere on Cirrus navigates back to Ask Cirrus

### Products Catalog
- 19 Cloudflare products with official links to cloudflare.com / developers.cloudflare.com
- Grouped: AI Platform first · Core Products · Plans last
- Section labels, hover arrow (↗), cursor pointer

### Security Audit Tool
- Visual score cards: Performance · Security · Availability
- Labels per score: Critical (< 65) · Needs work (65–84) · Good (85+)
- Structured result cards: Security Gaps · Performance Improvements · AI Opportunities · Cost Summary
- Urgency badges on security items: Critical / Recommended
- AI Opportunities tailored to the site's detected use case
- "Ask Cirrus for a deeper analysis" → auto-navigates to chat and sends pre-filled message

### Cost Calculator
- Inputs: visitors/month · site type · storage · current Cloudflare situation
- AI Opportunities section always rendered, contextual by site type
- "Ask Cirrus to refine my plan" → auto-sends full profile to the agent

### Live News Feed
- `fetch-news.js` fetches and parses Cloudflare Blog + Changelog RSS in the Worker
- Extracts: title, link, pubDate, description (HTML stripped via `.split('<')[0]`)
- Rendered as cards: source badge (BLOG / CHANGELOG) · date · clickable title (↗)

### Navigation
- `history.pushState()` on every section change
- `popstate` listener for browser back/forward
- Section hash restored on page reload
- Clean URL on home: `#agent` is replaced with empty string

### Mission Control (Hidden)
- URL: `focuseffect.fr/#csm-cirrus-internal`
- CSM tooling mockup: QBR generator, renewal alerts, anomaly detection, smart upsell
- Dedicated Cirrus chat in CSM mode

---

## Project Structure

```
/
├── src/
│   ├── index.js           ← Worker — chat endpoint, news endpoint, KV memory
│   ├── cloudflare-data.js ← Cloudflare product data (export: CLOUDFLARE_PRICING)
│   └── fetch-news.js      ← RSS parser — Blog + Changelog (export: fetchCloudflareNews)
├── public/
│   └── index.html         ← Generated by write_site.py — do not edit directly
├── write_site.py          ← Python script that generates the full frontend
└── wrangler.jsonc         ← Workers config: KV binding, AI binding, compatibility date
```

---

## Deploy

**Prerequisites:** Cloudflare account · domain on Cloudflare · Node.js 18+ · Python 3

```bash
# Install Wrangler
npm install -g wrangler
wrangler login

# Create KV namespace for conversation memory
wrangler kv namespace create CACHE
# → copy the returned id into wrangler.jsonc under kv_namespaces

# Configure wrangler.jsonc
{
  "name": "your-worker-name",
  "main": "src/index.js",
  "compatibility_date": "2024-01-01",
  "kv_namespaces": [{ "binding": "CACHE", "id": "YOUR_KV_ID" }],
  "ai": { "binding": "AI" }
}

# Create AI Gateway
# Dashboard → AI → AI Gateway → create a gateway with id "default"

# Deploy Worker
npx wrangler deploy

# Generate frontend and deploy to Pages
# ⚠️ Always run write_site.py BEFORE wrangler pages deploy
python3 write_site.py
npx wrangler pages deploy public --project-name YOUR-PROJECT-NAME

# Add custom domain
# Pages dashboard → your project → Custom domains → Add custom domain
# Cloudflare auto-creates the DNS CNAME — no manual setup needed

# Full redeploy in one command
npx wrangler deploy && python3 write_site.py && npx wrangler pages deploy public --project-name YOUR-PROJECT-NAME
```

---

## ⚠️ Known Gotchas

**1. JavaScript backslashes inside Python triple-quoted strings**

`write_site.py` embeds JavaScript inside Python `'''...'''` strings. Every `\` in JavaScript must be doubled in the Python source:

| Write in Python | Produces in JS | Status |
|---|---|---|
| `split('\\n')` | `split('\n')` | ✅ correct |
| `split('\n')` | raw newline character in string | ❌ SyntaxError |
| `replace(/\\d+/g, '')` | `replace(/\d+/g, '')` | ✅ correct |

If nav buttons stop responding after a change: open DevTools → Console → look for `SyntaxError` with a line number. 99% of the time it's an unescaped `\n` or `\d` in a string.

**2. Always run write_site.py before deploying Pages**

`wrangler pages deploy` uploads whatever is currently in `public/`. If you forget to run `write_site.py` first, you'll deploy a stale version of the frontend while the Worker is already updated. Always use the full one-liner above.

**3. AI Gateway cache**

Responses are cached for 3600s. During development, if Cirrus seems to return outdated answers, it may be serving a cached response from AI Gateway. You can disable caching temporarily by setting `skipCache: true` in `src/index.js`.

**4. Wrangler Pages warning about `pages_build_output_dir`**

You may see this warning when deploying:
```
▲ [WARNING] Pages now has wrangler.jsonc support... missing "pages_build_output_dir"
```
This is harmless — Wrangler ignores `wrangler.jsonc` for Pages when you pass the directory explicitly via CLI. The deploy succeeds normally.

**5. Model selection**

`@cf/qwen/qwen3-30b-a3b-fp8` was tested but caused frequent timeouts in production due to model size. Switched to `@cf/meta/llama-3.3-70b-instruct-fp8-fast` which offers a better speed/quality tradeoff for conversational use cases.

**6. Browser language vs message language**

The LLM tends to respond in the browser's UI language rather than the message language if not explicitly instructed. The system prompt enforces: detect language from the current message text only — ignore browser settings, previous messages, and the user's name origin.

---

## Key Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Edge-first architecture** | Every component runs across 330+ Cloudflare datacenters — no origin server |
| **AI at the edge** | LLM inference without GPU provisioning — Workers AI handles it natively |
| **Stateful edge functions** | Workers KV enables persistent memory across sessions without a traditional database |
| **AI platform depth** | System prompt covers Workers AI, AI Gateway, AI Search, Vectorize, Agents SDK, AutoRAG, Browser Rendering, MCP, Workflows, Durable Objects |
| **Zero-infrastructure deployment** | No EC2, no VPS, no Docker, no Kubernetes — just `wrangler deploy` |
| **Full-stack from one provider** | DNS, CDN, compute, AI inference, caching, storage, monitoring — all Cloudflare |
| **Multilingual AI** | Language detection and response in 6 languages including ZH and JA |
| **Real-time data** | RSS feeds from Cloudflare Blog + Changelog parsed and served live via Workers |
| **CSM tooling** | Hidden Mission Control section demonstrates customer success use cases |

---

## Cloudflare Products Count

**Actively deployed:** Pages · Workers · Workers AI · AI Gateway · Workers KV · DNS

**In system prompt knowledge base (30+):** AI Search · Vectorize · Agents SDK · AutoRAG · Browser Rendering · MCP Servers · Workflows · Durable Objects · WAF · DDoS Protection · Bot Management · Page Shield · Zero Trust · Magic Transit · Email Security · Turnstile · Rate Limiting · API Shield · Agile SASE · Web3 · CDN · Argo Smart Routing · Image Optimization · Load Balancing · Waiting Room · R2 · D1 · KV · Queues · Hyperdrive

---

*Built by Hafida — May 2026*  
*Powered by Cloudflare Workers AI · Hosted on Cloudflare Pages*

---

## License

MIT
