import os

with open('/Users/haflabghiel/Downloads/cirrus_character.svg') as _f:
    _svg_raw = _f.read()
CIRRUS_SVG = _svg_raw.replace('<svg ', '<svg class="cirrus-char" onclick="showSection(\'agent\')" ', 1)

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FocusEffect - Cirrus, your Cloudflare AI Expert</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --orange: #F97316;
  --orange-dim: rgba(249,115,22,0.15);
  --orange-border: rgba(249,115,22,0.25);
  --bg: #080810;
  --bg2: #0F0F1A;
  --bg3: #14141F;
  --text: #E8E8F0;
  --text-muted: rgba(232,232,240,0.45);
  --text-dim: rgba(232,232,240,0.25);
  --border: rgba(255,255,255,0.06);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Space Grotesk", sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background-image: linear-gradient(rgba(249,115,22,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(249,115,22,0.03) 1px, transparent 1px); background-size: 48px 48px; pointer-events: none; z-index: 0; }
nav { position: sticky; top: 0; z-index: 100; display: flex; align-items: center; justify-content: space-between; padding: 0 32px; height: 60px; background: rgba(8,8,16,0.9); backdrop-filter: blur(12px); border-bottom: 0.5px solid var(--orange-border); }
.logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
.logo-cloud { width: 36px; height: 24px; filter: drop-shadow(0 0 8px rgba(249,115,22,0.5)); }
.logo-wordmark { display: flex; flex-direction: column; gap: 1px; }
.logo-name { font-size: 15px; font-weight: 600; color: #fff; letter-spacing: -0.3px; line-height: 1; }
.logo-name span { color: var(--orange); }
.logo-sub { font-family: "JetBrains Mono", monospace; font-size: 8px; color: rgba(249,115,22,0.5); letter-spacing: 2px; line-height: 1; }
.nav-links { display: flex; align-items: center; gap: 2px; }
.nav-btn { background: transparent; border: none; color: var(--text-muted); font-family: "Space Grotesk", sans-serif; font-size: 13px; padding: 6px 14px; border-radius: 6px; cursor: pointer; transition: all 0.2s; }
.nav-btn:hover { color: var(--orange); background: var(--orange-dim); }
.nav-btn.active { color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); }
.section { display: none; position: relative; z-index: 1; }
.section.visible { display: block; }
.hero { padding: 56px 32px 40px; position: relative; overflow: hidden; }
.hero-top { text-align: center; margin-bottom: 32px; }
.hero-glow { position: absolute; top: -100px; left: 50%; transform: translateX(-50%); width: 700px; height: 400px; background: radial-gradient(ellipse, rgba(249,115,22,0.1) 0%, transparent 65%); pointer-events: none; }
.hero-cloud { margin: 0 auto 20px; display: block; filter: drop-shadow(0 0 20px rgba(249,115,22,0.4)); animation: float 4s ease-in-out infinite; }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
.hero h1 { font-size: 38px; font-weight: 700; line-height: 1.2; margin-bottom: 12px; letter-spacing: -0.8px; color: #fff; }
.hero h1 em { color: var(--orange); font-style: normal; }
.hero-sub { font-size: 15px; color: var(--text-muted); max-width: 480px; margin: 0 auto 28px; line-height: 1.65; }
.chat-wrap { width: 100%; max-width: 1000px; margin: 0 auto; background: var(--bg2); border: 0.5px solid var(--orange-border); border-radius: 18px; overflow: hidden; box-shadow: 0 0 40px rgba(249,115,22,0.08); }
.chat-header { padding: 14px 20px; display: flex; align-items: center; gap: 10px; border-bottom: 0.5px solid rgba(249,115,22,0.12); background: rgba(249,115,22,0.05); }
.chat-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--orange); box-shadow: 0 0 8px rgba(249,115,22,0.7); animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
.chat-title { font-size: 13px; color: rgba(255,255,255,0.7); font-weight: 500; }
.chat-title em { color: var(--orange); font-style: normal; }
.chat-badge { background: rgba(249,115,22,0.1); border: 0.5px solid var(--orange-border); color: var(--orange); font-size: 10px; padding: 3px 10px; border-radius: 20px; }
.chat-clear { background: transparent; border: 0.5px solid rgba(255,255,255,0.1); color: var(--text-dim); font-size: 11px; padding: 3px 10px; border-radius: 20px; cursor: pointer; margin-left: auto; font-family: "Space Grotesk", sans-serif; transition: all 0.2s; }
.chat-clear:hover { border-color: rgba(249,115,22,0.3); color: var(--orange); }
.chat-messages { padding: 20px; display: flex; flex-direction: column; gap: 12px; min-height: 200px; max-height: 460px; overflow-y: auto; }
.msg { padding: 14px 18px; border-radius: 14px; font-size: 13.5px; line-height: 1.7; max-width: 85%; animation: msgIn 0.3s ease; text-align: left; }
@keyframes msgIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.msg-ai { background: var(--bg3); border: 0.5px solid rgba(249,115,22,0.1); color: rgba(255,255,255,0.85); align-self: flex-start; }
.msg-ai strong { color: var(--orange); font-weight: 600; }
.msg-user { background: rgba(249,115,22,0.14); border: 0.5px solid rgba(249,115,22,0.3); color: #FFD4A8; align-self: flex-end; }
.msg-thinking { background: var(--bg3); border: 0.5px solid rgba(249,115,22,0.1); color: var(--text-muted); align-self: flex-start; font-style: italic; font-size: 12px; }
.chat-input-row { display: flex; gap: 8px; padding: 14px 16px; border-top: 0.5px solid rgba(249,115,22,0.1); }
#chat-input { flex: 1; background: var(--bg3); border: 0.5px solid rgba(249,115,22,0.2); border-radius: 10px; padding: 10px 15px; font-size: 13px; font-family: "Space Grotesk", sans-serif; color: #fff; outline: none; }
#chat-input::placeholder { color: var(--text-dim); }
#send-btn { background: var(--orange); color: #fff; border: none; border-radius: 10px; padding: 10px 24px; font-size: 13px; font-weight: 500; font-family: "Space Grotesk", sans-serif; cursor: pointer; }
#send-btn:disabled { opacity: 0.4; cursor: not-allowed; }
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; padding: 32px; max-width: 1100px; margin: 0 auto; }
.feat-card { background: var(--bg2); border: 0.5px solid var(--border); border-radius: 14px; padding: 22px; cursor: pointer; transition: all 0.2s; }
.feat-card:hover { border-color: var(--orange-border); background: var(--bg3); }
.feat-icon { font-size: 22px; margin-bottom: 12px; }
.feat-title { font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.85); margin-bottom: 6px; }
.feat-desc { font-size: 12px; color: var(--text-muted); line-height: 1.5; }
.feat-card.csm-card { border-color: rgba(249,115,22,0.15); background: rgba(249,115,22,0.03); }
.feat-card.csm-card .feat-title { color: rgba(249,115,22,0.65); }
.page-header { padding: 52px 32px 32px; max-width: 1100px; margin: 0 auto; }
.page-header h2 { font-size: 28px; font-weight: 700; color: #fff; letter-spacing: -0.5px; margin-bottom: 8px; }
.page-header h2 em { color: var(--orange); font-style: normal; }
.page-header p { font-size: 14px; color: var(--text-muted); line-height: 1.6; }
.products-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; padding: 0 32px 40px; max-width: 1100px; margin: 0 auto; }
.product-card { background: var(--bg2); border: 0.5px solid var(--border); border-radius: 14px; padding: 20px; transition: border-color 0.2s; cursor:pointer; position:relative; }
.product-card:hover { border-color: var(--orange-border); }
.card-arrow { position:absolute; top:10px; right:12px; font-size:13px; color:var(--orange); opacity:0; transition:opacity 0.2s; }
.product-card:hover .card-arrow { opacity:1; }
.product-group-label { grid-column: 1/-1; font-size:11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:rgba(249,115,22,0.7); padding:8px 0 4px; border-bottom:0.5px solid rgba(249,115,22,0.15); margin-bottom:4px; }
.product-name { font-size: 14px; font-weight: 600; color: #fff; margin-bottom: 6px; }
.product-desc { font-size: 12px; color: var(--text-muted); margin-bottom: 12px; line-height: 1.5; }
.product-price { font-family: "JetBrains Mono", monospace; font-size: 11px; color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); padding: 3px 10px; border-radius: 6px; display: inline-block; }
.plan-tag { font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 4px; letter-spacing: 0.5px; display: inline-block; margin-bottom: 8px; }
.tag-free { background: rgba(34,197,94,0.12); color: #4ade80; border: 0.5px solid rgba(34,197,94,0.25); }
.tag-pro { background: rgba(249,115,22,0.12); color: #fb923c; border: 0.5px solid var(--orange-border); }
.tag-biz { background: rgba(168,85,247,0.12); color: #c084fc; border: 0.5px solid rgba(168,85,247,0.25); }
.tag-ent { background: rgba(250,204,21,0.12); color: #fbbf24; border: 0.5px solid rgba(250,204,21,0.25); }
.calc-wrap { max-width: 680px; margin: 0 auto; padding: 0 32px 40px; }
.calc-card { background: var(--bg2); border: 0.5px solid var(--border); border-radius: 16px; padding: 28px; margin-bottom: 16px; }
.calc-card h3 { font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 20px; }
.form-row { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
.form-row label { font-size: 12px; color: var(--text-muted); font-weight: 500; }
.form-row input, .form-row select { background: var(--bg3); border: 0.5px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 14px; font-size: 13px; font-family: "Space Grotesk", sans-serif; color: #fff; outline: none; }
.form-row select option { background: var(--bg3); }
.calc-btn { width: 100%; background: var(--orange); color: #fff; border: none; border-radius: 10px; padding: 12px; font-size: 14px; font-weight: 600; font-family: "Space Grotesk", sans-serif; cursor: pointer; margin-top: 8px; }
.calc-result { background: var(--bg3); border: 0.5px solid var(--orange-border); border-radius: 12px; padding: 20px; display: none; }
.calc-result.show { display: block; }
.result-title { font-size: 13px; color: var(--text-muted); margin-bottom: 12px; }
.result-total { font-size: 32px; font-weight: 700; color: var(--orange); font-family: "JetBrains Mono", monospace; margin-bottom: 8px; }
.result-line { font-size: 12px; color: var(--text-muted); padding: 4px 0; border-bottom: 0.5px solid var(--border); display: flex; justify-content: space-between; }
.result-line span { color: rgba(255,255,255,0.7); }
.ai-opps-section { margin-top: 24px; }
.ai-opps-title { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(249,115,22,0.7); padding-bottom: 10px; border-bottom: 0.5px solid rgba(249,115,22,0.15); margin-bottom: 14px; }
.ai-opps-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.ai-opp-card { background: var(--bg2); border: 0.5px solid rgba(249,115,22,0.2); border-radius: 12px; padding: 14px; cursor: pointer; transition: border-color 0.2s; text-decoration: none; display: block; }
.ai-opp-card:hover { border-color: var(--orange-border); }
.ai-opp-tag { font-size: 9px; font-weight: 700; letter-spacing: 1px; color: var(--orange); opacity: 0.8; margin-bottom: 4px; }
.ai-opp-name { font-size: 13px; font-weight: 600; color: #fff; margin-bottom: 4px; }
.ai-opp-desc { font-size: 11px; color: var(--text-muted); line-height: 1.5; margin-bottom: 8px; }
.ai-opp-price { font-family: "JetBrains Mono", monospace; font-size: 10px; color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); padding: 2px 8px; border-radius: 5px; display: inline-block; }
.cirrus-plan-btn { width: 100%; background: transparent; color: var(--orange); border: 0.5px solid var(--orange-border); border-radius: 10px; padding: 11px; font-size: 13px; font-weight: 600; font-family: "Space Grotesk", sans-serif; cursor: pointer; margin-top: 16px; transition: background 0.2s; }
.cirrus-plan-btn:hover { background: var(--orange-dim); }
.cirrus-plan-result { margin-top: 16px; background: var(--bg2); border: 0.5px solid var(--orange-border); border-radius: 12px; padding: 18px; font-size: 13px; color: rgba(255,255,255,0.85); line-height: 1.7; display: none; }
.cirrus-plan-result.show { display: block; }
.news-wrap { max-width: 900px; margin: 0 auto; padding: 0 32px 40px; display: flex; flex-direction: column; gap: 12px; }
.news-card { background: var(--bg2); border: 0.5px solid var(--border); border-radius: 14px; padding: 20px; display: flex; gap: 16px; align-items: flex-start; transition: border-color 0.2s; }
.news-card:hover { border-color: var(--orange-border); }
.news-source { font-family: "JetBrains Mono", monospace; font-size: 10px; color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); padding: 3px 8px; border-radius: 4px; white-space: nowrap; margin-top: 2px; }
.news-content { flex: 1; }
.news-title { font-size: 14px; font-weight: 500; color: rgba(255,255,255,0.85); margin-bottom: 5px; line-height: 1.4; }
.news-date { font-size: 11px; color: var(--text-dim); font-family: "JetBrains Mono", monospace; }
.news-wrap a { color: inherit; }
.news-wrap a:hover .news-title { color: var(--orange); }
.news-loading { text-align: center; padding: 40px; color: var(--text-muted); font-size: 14px; }
.ticker-bar { background: var(--bg2); border-top: 0.5px solid rgba(249,115,22,0.12); padding: 10px 32px; display: flex; align-items: center; gap: 14px; position: relative; z-index: 1; overflow: hidden; }
.live-badge { background: var(--orange); color: #fff; font-size: 9px; font-weight: 700; padding: 2px 7px; border-radius: 4px; letter-spacing: 1px; white-space: nowrap; flex-shrink: 0; }
.ticker-track { display: flex; white-space: nowrap; animation: ticker-scroll 60s linear infinite; }
.ticker-track:hover { animation-play-state: paused; }
.ticker-text { font-size: 12px; color: var(--text-dim); white-space: nowrap; }
.ticker-text strong { color: rgba(249,115,22,0.65); font-weight: 500; }
@keyframes ticker-scroll { 0% { transform: translateX(100vw); } 100% { transform: translateX(-100%); } }
.csm-wrap { max-width: 700px; margin: 0 auto; padding: 0 32px 40px; }
.csm-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 24px; }
.csm-card { background: var(--bg2); border: 0.5px solid rgba(249,115,22,0.15); border-radius: 14px; padding: 20px; }
.csm-card h4 { font-size: 13px; font-weight: 600; color: rgba(249,115,22,0.8); margin-bottom: 6px; }
.csm-card p { font-size: 12px; color: var(--text-muted); line-height: 1.5; }
.csm-chat-wrap { background: var(--bg2); border: 0.5px solid rgba(249,115,22,0.2); border-radius: 16px; overflow: hidden; }
.csm-chat-header { padding: 12px 18px; border-bottom: 0.5px solid rgba(249,115,22,0.12); background: rgba(249,115,22,0.06); font-size: 12px; color: rgba(249,115,22,0.7); font-family: "JetBrains Mono", monospace; letter-spacing: 0.5px; }
.csm-messages { padding: 16px; display: flex; flex-direction: column; gap: 10px; min-height: 120px; max-height: 260px; overflow-y: auto; }
.csm-input-row { display: flex; gap: 8px; padding: 12px 14px; border-top: 0.5px solid rgba(249,115,22,0.1); }
#csm-input { flex: 1; background: var(--bg3); border: 0.5px solid rgba(249,115,22,0.2); border-radius: 8px; padding: 9px 14px; font-size: 13px; font-family: "Space Grotesk", sans-serif; color: #fff; outline: none; }
#csm-input::placeholder { color: var(--text-dim); }
#csm-send { background: rgba(249,115,22,0.8); color: #fff; border: none; border-radius: 8px; padding: 9px 18px; font-size: 13px; font-family: "Space Grotesk", sans-serif; cursor: pointer; }
.audit-wrap { max-width: 1000px; margin: 0 auto; padding: 0 32px 40px; }
.audit-card { background: var(--bg2); border: 0.5px solid var(--border); border-radius: 16px; padding: 28px; }
.audit-card h3 { font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 20px; }
.audit-result { margin-top: 20px; display: none; }
.audit-result.show { display: block; }
.score-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 16px; }
.score-card { background: var(--bg3); border: 0.5px solid var(--border); border-radius: 10px; padding: 14px; text-align: center; }
.score-val { font-size: 26px; font-weight: 700; font-family: "JetBrains Mono", monospace; margin-bottom: 4px; }
.score-val.good { color: #4ade80; }
.score-val.mid { color: #fbbf24; }
.score-val.bad { color: #f87171; }
.score-label { font-size: 11px; color: var(--text-muted); }
.audit-sections { display: flex; flex-direction: column; gap: 12px; margin-top: 16px; }
.audit-section { background: var(--bg3); border: 0.5px solid var(--border); border-radius: 12px; overflow: hidden; }
.audit-section-header { display: flex; align-items: center; gap: 10px; padding: 12px 16px; border-bottom: 0.5px solid var(--border); background: rgba(255,255,255,0.02); }
.audit-section-icon { width: 28px; height: 28px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 14px; }
.audit-section-title { font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.85); }
.audit-section-body { padding: 12px 16px; }
.audit-product-row { display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 0.5px solid var(--border); }
.audit-product-row:last-child { border-bottom: none; }
.audit-product-name { font-size: 13px; font-weight: 500; color: rgba(255,255,255,0.85); }
.audit-price-tag { font-size: 11px; color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); padding: 3px 8px; border-radius: 20px; white-space: nowrap; }
.audit-total { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; background: rgba(249,115,22,0.05); border-top: 0.5px solid rgba(249,115,22,0.15); }
.audit-total-label { font-size: 13px; font-weight: 500; color: rgba(255,255,255,0.7); }
.audit-total-amount { font-size: 18px; font-weight: 700; color: var(--orange); font-family: "JetBrains Mono", monospace; }
.audit-improvement-row { display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 0.5px solid var(--border); }
.audit-improvement-row:last-child { border-bottom: none; }
.audit-badge-green { font-size: 11px; color: #4ade80; background: rgba(34,197,94,0.1); border: 0.5px solid rgba(34,197,94,0.25); padding: 3px 8px; border-radius: 20px; }
.audit-site-header { display: flex; align-items: center; gap: 12px; padding: 14px 16px; background: rgba(249,115,22,0.04); border-bottom: 0.5px solid var(--border); border-radius: 12px; }
.audit-not-cf { font-size: 10px; color: var(--orange); background: var(--orange-dim); border: 0.5px solid var(--orange-border); padding: 2px 8px; border-radius: 20px; margin-left: auto; white-space: nowrap; }
.score-card.bad-border { border-color: rgba(248,113,113,0.4); }
.score-card.mid-border { border-color: rgba(251,191,36,0.4); }
.score-card.good-border { border-color: rgba(74,222,128,0.35); }
.score-status { font-size: 10px; font-weight: 700; letter-spacing: 0.5px; margin-top: 6px; padding: 2px 8px; border-radius: 20px; display: inline-block; }
.score-status.critical { color: #f87171; background: rgba(248,113,113,0.12); }
.score-status.needs-work { color: #fbbf24; background: rgba(251,191,36,0.1); }
.score-status.sgreen { color: #4ade80; background: rgba(74,222,128,0.1); }
.audit-result-grid { display: flex; flex-direction: column; gap: 14px; margin-top: 20px; }
.audit-block { background: var(--bg3); border-radius: 14px; overflow: hidden; border: 0.5px solid var(--border); }
.audit-block-security { border-left: 3px solid rgba(248,113,113,0.6); }
.audit-block-perf { border-left: 3px solid rgba(249,115,22,0.6); }
.audit-block-ai { border-left: 3px solid rgba(139,92,246,0.7); }
.audit-block-cost { border-left: 3px solid rgba(74,222,128,0.5); }
.audit-block-hd { display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-bottom: 0.5px solid var(--border); }
.audit-block-icon { width: 32px; height: 32px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0; }
.audit-block-title { font-size: 14px; font-weight: 700; color: #fff; }
.audit-block-subtitle { font-size: 11px; color: var(--text-muted); margin-top: 2px; }
.audit-block-body { padding: 14px 18px; display: flex; flex-direction: column; gap: 0; }
.audit-gap-row { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 0.5px solid var(--border); }
.audit-gap-row:last-child { border-bottom: none; padding-bottom: 0; }
.audit-gap-icon { font-size: 16px; flex-shrink: 0; margin-top: 1px; }
.audit-gap-content { flex: 1; }
.audit-gap-name { font-size: 13px; font-weight: 600; color: #fff; }
.audit-gap-desc { font-size: 11px; color: var(--text-muted); margin-top: 2px; line-height: 1.4; }
.audit-gap-meta { display: flex; align-items: center; gap: 8px; margin-top: 6px; flex-wrap: wrap; }
.badge-critical { font-size: 9px; font-weight: 700; letter-spacing: 0.8px; color: #f87171; background: rgba(248,113,113,0.12); border: 0.5px solid rgba(248,113,113,0.3); padding: 2px 7px; border-radius: 20px; }
.badge-rec { font-size: 9px; font-weight: 700; letter-spacing: 0.8px; color: #fbbf24; background: rgba(251,191,36,0.1); border: 0.5px solid rgba(251,191,36,0.3); padding: 2px 7px; border-radius: 20px; }
.audit-ai-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.audit-cost-row { display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 0.5px solid var(--border); }
.audit-cost-row:last-child { border-bottom: none; }
.audit-cost-total { display: flex; align-items: center; justify-content: space-between; padding: 14px 18px; background: rgba(249,115,22,0.05); border-top: 0.5px solid rgba(249,115,22,0.15); }
.audit-summary-line { font-size: 11px; color: var(--text-muted); font-style: italic; margin-top: 3px; }
.audit-deeper-btn { width: 100%; background: transparent; color: var(--orange); border: 0.5px solid var(--orange-border); border-radius: 10px; padding: 12px; font-size: 13px; font-weight: 600; font-family: "Space Grotesk", sans-serif; cursor: pointer; margin-top: 16px; transition: background 0.2s; }
.audit-deeper-btn:hover { background: var(--orange-dim); }
@media (max-width: 700px) {
  nav { padding: 0 16px; }
  .hero { padding: 36px 16px 24px; }
  .hero h1 { font-size: 26px; }
  .features-grid { grid-template-columns: 1fr 1fr; padding: 16px; }
  .products-grid { padding: 0 16px 32px; }
  .calc-wrap, .audit-wrap, .csm-wrap, .news-wrap { padding: 0 16px 32px; }
  .csm-grid { grid-template-columns: 1fr; }
  .page-header { padding: 36px 16px 24px; }
}
@keyframes cirrus-float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-7px)} }
.cirrus-char { width:160px; animation: cirrus-float 3.5s ease-in-out infinite; filter: drop-shadow(0 0 6px rgba(249,115,22,0.8)) drop-shadow(0 0 14px rgba(249,115,22,0.35)); cursor:pointer; }
.cirrus-bubble { background:#0F0F1A; border:0.5px solid rgba(249,115,22,0.4); border-radius:14px 14px 14px 0; padding:10px 14px; font-size:12px; color:rgba(255,255,255,0.85); max-width:180px; line-height:1.5; position:relative; }
.cirrus-wrap { display:flex; align-items:flex-end; gap:12px; }
.cirrus-bubble-wrap { display:flex; flex-direction:column; gap:8px; padding-bottom:20px; }
.cirrus-corner { position:fixed; bottom:24px; right:24px; z-index:999; display:none; flex-direction:column; align-items:flex-end; gap:8px; }
.cirrus-corner.visible { display:flex; }
.cirrus-corner .cirrus-bubble { border-radius:14px 14px 0 14px; }
@keyframes fadeIn { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.cirrus-corner { animation: fadeIn 0.4s ease; }
</style>
</head>
<body>
<nav>
  <a class="logo" href="#" onclick="showSection('agent'); return false;">
    <svg class="logo-cloud" viewBox="0 0 36 24" fill="none">
      <ellipse cx="18" cy="17" rx="16" ry="7" fill="#F97316" opacity="0.9"/>
      <ellipse cx="12" cy="14" rx="9" ry="8" fill="#F97316"/>
      <ellipse cx="24" cy="13" rx="8" ry="7" fill="#FB923C"/>
      <ellipse cx="18" cy="10" rx="8" ry="7" fill="#FDBA74"/>
      <ellipse cx="18" cy="18" rx="16" ry="4" fill="#080810" opacity="0.5"/>
    </svg>
    <div class="logo-wordmark">
      <div class="logo-name">Focus<span>Effect</span></div>
      <div class="logo-sub">POWERED BY CIRRUS</div>
    </div>
  </a>
  <div class="nav-links">
    <button class="nav-btn active" id="btn-agent" onclick="showSection('agent')">Ask Cirrus</button>
    <button class="nav-btn" id="btn-produits" onclick="showSection('produits')">Products</button>
    <button class="nav-btn" id="btn-calculateur" onclick="showSection('calculateur')">Calculator</button>
    <button class="nav-btn" id="btn-audit" onclick="showSection('audit')">Audit</button>
    <button class="nav-btn" id="btn-actualites" onclick="showSection('actualites')">News</button>
  </div>
</nav>

<section id="section-agent" class="section visible">
  <div class="hero">
    <div class="hero-glow"></div>
    <div class="hero-top">
      <svg class="hero-cloud" width="72" height="46" viewBox="0 0 80 52" fill="none">
        <ellipse cx="40" cy="36" rx="36" ry="15" fill="#F97316" opacity="0.9"/>
        <ellipse cx="26" cy="30" rx="20" ry="17" fill="#F97316"/>
        <ellipse cx="54" cy="28" rx="18" ry="15" fill="#FB923C"/>
        <ellipse cx="40" cy="22" rx="17" ry="15" fill="#FDBA74"/>
        <ellipse cx="40" cy="38" rx="36" ry="8" fill="#080810" opacity="0.5"/>
      </svg>
      <h1>Your <em>Cloudflare</em> expert<br>powered by Cirrus</h1>
      <p class="hero-sub">Product recommendations, cost calculation, optimization and performance audit - official real-time data.</p>
    </div>
    <div style="display:flex;align-items:flex-end;justify-content:center;gap:24px;max-width:1200px;margin:0 auto;">
      <div class="cirrus-bubble-wrap">
        <div class="cirrus-bubble">Hey! Ask me anything,<br>I live in 330 datacenters and I never sleep 😄</div>
        __CIRRUS__
      </div>
      <div class="chat-wrap" style="flex:1;">
        <div class="chat-header">
          <div class="chat-dot"></div>
          <span class="chat-title"><em>Cirrus</em> - Cloudflare Expert</span>
          <span class="chat-badge">ONLINE</span>
          <button class="chat-clear" onclick="clearConversation()">Clear chat</button>
        </div>
        <div class="chat-messages" id="chat-messages"></div>
        <div class="chat-input-row">
          <input type="text" id="chat-input" placeholder="Describe your project or ask a question..." />
          <button id="send-btn" onclick="sendMessage()">Send</button>
        </div>
      </div>
    </div>
  </div>
  <div class="features-grid">
    <div class="feat-card" onclick="showSection('audit')"><div class="feat-icon">&#9889;</div><div class="feat-title">Performance Audit</div><div class="feat-desc">Speed, Core Web Vitals, WAF security - complete real-time site analysis</div></div>
    <div class="feat-card" onclick="showSection('calculateur')"><div class="feat-icon">&#128176;</div><div class="feat-title">Cost Calculator</div><div class="feat-desc">Precise simulation based on your traffic with quantified savings</div></div>
    <div class="feat-card" onclick="showSection('produits')"><div class="feat-icon">&#128200;</div><div class="feat-title">Optimization</div><div class="feat-desc">Current vs optimized plan - discover what you are losing every month</div></div>
    <div class="feat-card" onclick="showSection('actualites')"><div class="feat-icon">&#128276;</div><div class="feat-title">Live News</div><div class="feat-desc">Blog, changelog and announcements in real time</div></div>
    <div class="feat-card" onclick="showSection('produits')"><div class="feat-icon">&#128230;</div><div class="feat-title">Product Catalog</div><div class="feat-desc">All products with official pricing and use cases</div></div>
    <div class="feat-card csm-card"><div class="feat-icon">&#128274;</div><div class="feat-title">Mission Control</div><div class="feat-desc">Restricted access — private link</div></div>
  </div>
</section>

<section id="section-produits" class="section">
  <div class="page-header"><h2>Cloudflare <em>Catalog</em></h2><p>All products with updated official pricing.</p></div>
  <div class="products-grid">
    <div class="product-group-label">AI Platform</div>
    <div class="product-card" onclick="window.open('https://ai.cloudflare.com/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">WORKERS AI</span><div class="product-name">Workers AI</div><div class="product-desc">50+ AI models at the edge. Pay only for CPU time, not wall time.</div><span class="product-price">$0.011/1K neurons</span></div>
    <div class="product-card" onclick="window.open('https://developers.cloudflare.com/ai-gateway/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">AI GATEWAY</span><div class="product-name">AI Gateway</div><div class="product-desc">Observe, cache and control all AI requests, any provider.</div><span class="product-price">Free</span></div>
    <div class="product-card" onclick="window.open('https://developers.cloudflare.com/ai-search/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">AI SEARCH</span><div class="product-name">AI Search (Beta)</div><div class="product-desc">Managed RAG, connect your site or R2, get semantic search instantly.</div><span class="product-price">Free tier available</span></div>
    <div class="product-card" onclick="window.open('https://developers.cloudflare.com/vectorize/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">VECTORIZE</span><div class="product-name">Vectorize</div><div class="product-desc">Vector database for semantic search and RAG pipelines.</div><span class="product-price">Free: 30M dimensions</span></div>
    <div class="product-card" onclick="window.open('https://developers.cloudflare.com/agents/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">AGENTS SDK</span><div class="product-name">Cloudflare Agents</div><div class="product-desc">Build autonomous AI agents with memory, tools and scheduling.</div><span class="product-price">Included with Workers</span></div>
    <div class="product-group-label">Core Products</div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/lp/pg-cdn-performance-bundle-3-v2/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">FREE</span><div class="product-name">CDN Global</div><div class="product-desc">330+ datacenters, automatic caching, sub-10ms DNS.</div><span class="product-price">Free</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/ddos/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">FREE</span><div class="product-name">DDoS Protection</div><div class="product-desc">Unmetered, automatic, always-on. 321 Tbps+ network capacity.</div><span class="product-price">Free</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/ssl/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">FREE</span><div class="product-name">SSL/TLS</div><div class="product-desc">Universal SSL, automatic HTTPS, end-to-end encryption.</div><span class="product-price">Free</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/turnstile/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">FREE</span><div class="product-name">Turnstile (CAPTCHA)</div><div class="product-desc">Privacy-first CAPTCHA alternative. No tracking.</div><span class="product-price">1M/month free</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/zero-trust/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">ZERO TRUST</span><div class="product-name">Zero Trust / SASE</div><div class="product-desc">Replace VPN with Access + Tunnel + WARP. Free up to 50 users.</div><span class="product-price">Free up to 50 users</span></div>
    <div class="product-card" onclick="window.open('https://workers.cloudflare.com/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">WORKERS</span><div class="product-name">Cloudflare Workers</div><div class="product-desc">Serverless at the edge in 330+ locations, under 1ms cold start.</div><span class="product-price">$5/mo + $0.50/M req</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/r2/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">R2 STORAGE</span><div class="product-name">Cloudflare R2</div><div class="product-desc">S3-compatible storage with ZERO egress fees.</div><span class="product-price">$0.015/GB/month</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/argo-smart-routing/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">ARGO</span><div class="product-name">Argo Smart Routing</div><div class="product-desc">Intelligent routing avoiding congested paths. ~30% faster.</div><span class="product-price">$5/mo + $0.10/GB</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/sase/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">SASE</span><div class="product-name">The Agile SASE Platform</div><div class="product-desc">Secure Access Service Edge — network security and connectivity in one platform.</div><span class="product-price">Custom pricing</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/bot-mitigation/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">SECURITY</span><div class="product-name">Bot Management</div><div class="product-desc">Machine learning bot detection. Stops credential stuffing, scraping and fake traffic.</div><span class="product-price">Business+</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/products/web3/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-free">WEB3</span><div class="product-name">Web3</div><div class="product-desc">Decentralized web infrastructure — IPFS and Ethereum gateways at the edge.</div><span class="product-price">Free tier available</span></div>
    <div class="product-group-label">Plans</div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/plans/pro/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-pro">PRO</span><div class="product-name">Pro Plan</div><div class="product-desc">WAF managed rules, image optimization, 25 Page Rules.</div><span class="product-price">$20/month per domain</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/plans/business/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-biz">BUSINESS</span><div class="product-name">Business Plan</div><div class="product-desc">Custom WAF, 100% uptime SLA, PCI compliance, Bot Management.</div><span class="product-price">$200/month per domain</span></div>
    <div class="product-card" onclick="window.open('https://www.cloudflare.com/plans/enterprise/','_blank')"><span class="card-arrow">&#8599;</span><span class="plan-tag tag-ent">ENTERPRISE</span><div class="product-name">Enterprise Plan</div><div class="product-desc">Dedicated CSM, custom SLA, unlimited rules, Magic Transit.</div><span class="product-price">Custom pricing</span></div>
  </div>
  <p style="text-align:center;font-size:11px;color:var(--text-dim);padding:16px 32px 8px;">* This catalog covers the main Cloudflare products. The full portfolio includes 100+ products and services — ask Cirrus for anything not listed here.</p>
</section>

<section id="section-calculateur" class="section">
  <div class="page-header"><h2>Cost <em>Calculator</em></h2><p>Estimate your budget. Results based on official pricing.</p></div>
  <div class="calc-wrap">
    <div class="calc-card">
      <h3>Your profile</h3>
      <div class="form-row"><label>Visitors per month</label><input type="number" id="calc-visitors" placeholder="ex: 50000" value="50000"></div>
      <div class="form-row"><label>Site type</label><select id="calc-type"><option value="blog">Blog / Showcase site</option><option value="ecom" selected>E-commerce</option><option value="saas">SaaS / Web application</option><option value="media">Media / Video</option><option value="api">API / Developer</option></select></div>
      <div class="form-row"><label>Current situation</label><select id="calc-situation"><option value="new">Not yet on Cloudflare</option><option value="free">Cloudflare Free Plan</option><option value="pro">Cloudflare Pro Plan</option><option value="business">Cloudflare Business Plan</option></select></div>
      <div class="form-row"><label>Estimated storage (GB)</label><input type="number" id="calc-storage" placeholder="ex: 10" value="10"></div>
      <button class="calc-btn" onclick="calculateCost()">Calculate my budget</button>
    </div>
    <div class="calc-result" id="calc-result">
      <div class="result-title">Recommended monthly estimate</div>
      <div class="result-total" id="result-total">$0/month</div>
      <div id="result-lines"></div>
      <div class="ai-opps-section">
        <div class="ai-opps-title">&#9889; AI Opportunities for your profile</div>
        <div class="ai-opps-grid" id="ai-opps-grid"></div>
      </div>
      <button class="cirrus-plan-btn" onclick="askCirrusPlan()">&#10024; Ask Cirrus for a detailed plan</button>
      <div class="cirrus-plan-result" id="cirrus-plan-result"></div>
    </div>
  </div>
</section>

<section id="section-audit" class="section">
  <div class="page-header"><h2>Performance <em>Audit</em></h2><p>Enter your site URL - Cirrus analyzes and recommends the right optimizations.</p></div>
  <div class="audit-wrap">
    <div class="audit-card">
      <h3>Analyze a site</h3>
      <div class="form-row"><label>Your site URL</label><input type="text" id="audit-url" placeholder="https://yourwebsite.com"></div>
      <div class="form-row"><label>Current issues (optional)</label><select id="audit-issues"><option value="speed">Slow speed / loading time</option><option value="security">Security issues / attacks</option><option value="cost">High bandwidth costs</option><option value="downtime">Downtime / availability</option><option value="all">Full audit</option></select></div>
      <button class="calc-btn" onclick="runAudit()">Run audit with Cirrus</button>
      <div class="audit-result" id="audit-result">
        <div class="score-grid" id="score-grid"></div>
        <div id="audit-cards"></div>
      </div>
    </div>
  </div>
</section>

<section id="section-actualites" class="section">
  <div class="page-header"><h2>Cloudflare <em>News</em></h2><p>Official blog and product changelog - updated in real time.</p></div>
  <div class="news-wrap" id="news-wrap"><div class="news-loading">Loading Cloudflare news...</div></div>
</section>

<section id="section-csm" class="section">
  <div class="page-header"><h2>CSM <em>Space</em> - Internal use</h2><p>Tools reserved for Cloudflare Customer Success Managers.</p></div>
  <div class="csm-wrap">
    <div class="csm-grid">
      <div class="csm-card"><h4>Automatic QBR</h4><p>Generate a complete quarterly report for your clients in seconds.</p></div>
      <div class="csm-card"><h4>Renewal alerts</h4><p>Identify at-risk contracts and upsell opportunities in real time.</p></div>
      <div class="csm-card"><h4>Anomaly detection</h4><p>Alerts if a client is under DDoS attack or exceeds usage thresholds.</p></div>
      <div class="csm-card"><h4>Smart upsell</h4><p>Cirrus identifies missing products and calculates ROI.</p></div>
    </div>
    <div class="csm-chat-wrap">
      <div class="csm-chat-header">CIRRUS CSM MODE - INTERNAL ACCESS</div>
      <div class="csm-messages chat-messages" id="csm-messages">
        <div class="msg msg-ai">CSM mode activated. I can generate QBR reports, analyze client portfolios, detect upsell opportunities and prepare renewals. How can I help?</div>
      </div>
      <div class="csm-input-row">
        <input type="text" id="csm-input" placeholder="Ex: Generate a QBR for client Acme Corp...">
        <button id="csm-send" onclick="sendCSMMessage()">Send</button>
      </div>
    </div>
  </div>
</section>

<div class="ticker-bar">
  <span class="live-badge">LIVE</span>
  <div class="ticker-track" id="ticker-track">
    <span class="ticker-text" id="ticker-text">&nbsp;</span>
  </div>
</div>

<script>
const WORKER_URL = 'https://focuseffect-agent.hafida0203492.workers.dev';
const STORAGE_KEY = 'cirrus_conversation';
const USER_KEY = 'cirrus_user';

const WELCOME_MESSAGES = [
  'Hey, I am Cirrus. I live in 330 datacenters simultaneously and I have never had a slow day.\\nTell me about your website, and I will tell you exactly what is slowing it down, what is leaving it exposed, and what it would cost to fix - down to the cent.',
  'Cirrus here. Former cloud, current AI expert.\\nI know every product, every price, and every reason your infrastructure could be faster and safer. What are we fixing today?',
  'Good to see you. I have been running at full capacity across 330 edge locations while you were away.\\nWhat does your website need - more speed, better security, or is it time to add some AI?',
  'Initializing Cirrus... 330 edge nodes online. WAF armed. AI models warmed up.\\nYour website might not be ready. Tell me about it and let us find out together.',
  'Zero downtime. Zero slow days. That is how I operate.\\nNow - describe your project and I will tell you exactly what products will make the biggest difference, with exact prices.'
];

function getOrCreateUserId() {
  try {
    let user = localStorage.getItem(USER_KEY);
    if (!user) {
      user = JSON.stringify({ id: 'u_' + Math.random().toString(36).substr(2, 9), name: null });
      localStorage.setItem(USER_KEY, user);
    }
    return JSON.parse(user);
  } catch(e) { return { id: 'anonymous', name: null }; }
}

function saveUserName(name) {
  try {
    const user = getOrCreateUserId();
    user.name = name;
    localStorage.setItem(USER_KEY, JSON.stringify(user));
  } catch(e) {}
}

function detectName(text) {
  const patterns = [
    /(?:i(?:'|')?m|i am|my name is|call me|this is)\s+([A-Z][a-z]{1,20})/i,
    /^([A-Z][a-z]{1,20})\s+here\b/i
  ];
  for (const p of patterns) {
    const m = text.match(p);
    if (m) return m[1];
  }
  return null;
}

function getRandomWelcome(userName) {
  const msg = WELCOME_MESSAGES[Math.floor(Math.random() * WELCOME_MESSAGES.length)];
  if (userName) {
    return msg.replace('Hey, I am Cirrus.', 'Hey ' + userName + ', I am Cirrus.').replace('Good to see you.', 'Good to see you again, ' + userName + '.');
  }
  return msg;
}

function resolveSection(s) {
  const valid = {agent:1, produits:1, calculateur:1, audit:1, actualites:1};
  if (valid[s]) return s;
  const map = {
    ai:'produits', products:'produits', product:'produits', catalog:'produits',
    security:'produits', sase:'produits', cdn:'produits', ddos:'produits',
    news:'actualites', updates:'actualites', changelog:'actualites',
    calculator:'calculateur', pricing:'calculateur', costs:'calculateur', cost:'calculateur',
    chat:'agent', cirrus:'agent', home:'agent', ask:'agent',
    audit:'audit', performance:'audit'
  };
  return map[s.toLowerCase()] || 'agent';
}

function showSection(name) {
  document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  const section = document.getElementById('section-' + name);
  if (section) section.classList.add('visible');
  const activeBtn = document.getElementById('btn-' + name);
  if (activeBtn) activeBtn.classList.add('active');
  if (name === 'actualites') loadNews();
  window.scrollTo(0, 0);
  history.pushState(null, '', name === 'agent' ? '/' : '#' + name);
  updateCirrusCorner(name);
}

function formatMarkdown(text) {
  if (!text) return '';
  return text
    .replace(/—/g, ',')
    .replace(/^#### (.+)$/gm, '<br><strong style="font-size:13px;color:var(--orange);">$1</strong><br>')
    .replace(/^### (.+)$/gm, '<br><strong style="font-size:14px;color:var(--orange);">$1</strong><br>')
    .replace(/^## (.+)$/gm, '<br><strong style="font-size:15px;color:var(--orange);">$1</strong><br>')
    .replace(/^# (.+)$/gm, '<br><strong style="font-size:16px;color:var(--orange);">$1</strong><br>')
    .replace(/\\[([^\\]]+)\\]\\(#([^)]+)\\)/g, '<a href="#" onclick="showSection(resolveSection(\\'$2\\')); return false;" style="color:var(--orange);font-weight:600;text-decoration:none;border-bottom:1px solid rgba(249,115,22,0.4);">$1</a>')
    .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
    .replace(/\\*(.+?)\\*/g, '<em style="color:rgba(249,115,22,0.85);font-style:normal;">$1</em>')
    .replace(/^\\s*---+\\s*$/gm, '<hr style="border:none;border-top:0.5px solid rgba(249,115,22,0.2);margin:10px 0;">')
    .replace(/^\\s*[-\\*]\\s+(.+)$/gm, '<br>&#8226; $1')
    .replace(/\\n\\n/g, '<br><br>')
    .replace(/\\n/g, '<br>');
}

function saveConversation(messages) {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(messages)); } catch(e) {}
}

function loadConversation() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : null;
  } catch(e) { return null; }
}

function renderMessages(messages) {
  const msgs = document.getElementById('chat-messages');
  msgs.innerHTML = '';
  messages.forEach(m => {
    const div = document.createElement('div');
    div.className = m.type === 'user' ? 'msg msg-user' : 'msg msg-ai';
    if (m.type === 'ai') {
      div.innerHTML = formatMarkdown(m.text);
    } else {
      div.textContent = m.text;
    }
    msgs.appendChild(div);
  });
  msgs.scrollTop = msgs.scrollHeight;
}

function initChat() {
  const saved = loadConversation();
  const user = getOrCreateUserId();
  if (saved && saved.length > 0) {
    renderMessages(saved);
  } else {
    const welcomeText = getRandomWelcome(user.name);
    const msgs = document.getElementById('chat-messages');
    msgs.innerHTML = '';
    const div = document.createElement('div');
    div.className = 'msg msg-ai';
    div.innerHTML = formatMarkdown(welcomeText);
    msgs.appendChild(div);
    saveConversation([{ type: 'ai', text: welcomeText }]);
  }
}

function clearConversation() {
  try { localStorage.removeItem(STORAGE_KEY); } catch(e) {}
  const user = getOrCreateUserId();
  const welcomeText = getRandomWelcome(user.name);
  const msgs = document.getElementById('chat-messages');
  msgs.innerHTML = '';
  const div = document.createElement('div');
  div.className = 'msg msg-ai';
  div.innerHTML = formatMarkdown(welcomeText);
  msgs.appendChild(div);
  saveConversation([{ type: 'ai', text: welcomeText }]);
}

function addMessage(type, text) {
  const msgs = document.getElementById('chat-messages');
  const div = document.createElement('div');
  if (type === 'thinking') {
    div.className = 'msg msg-thinking';
    div.textContent = text;
  } else if (type === 'user') {
    div.className = 'msg msg-user';
    div.textContent = text;
  } else {
    div.className = 'msg msg-ai';
    div.innerHTML = formatMarkdown(text);
  }
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
  if (type !== 'thinking') {
    const saved = loadConversation() || [];
    saved.push({ type, text });
    saveConversation(saved);
  }
  return div;
}

async function sendMessage() {
  const input = document.getElementById('chat-input');
  const btn = document.getElementById('send-btn');
  const question = input.value.trim();
  if (!question) return;

  const detectedName = detectName(question);
  if (detectedName) saveUserName(detectedName);

  const user = getOrCreateUserId();
  addMessage('user', question);
  input.value = '';
  btn.disabled = true;
  const thinking = addMessage('thinking', 'Cirrus is thinking...');
  try {
    const res = await fetch(WORKER_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question, userId: user.id, userName: user.name })
    });
    const data = await res.json();
    thinking.remove();
    addMessage('ai', data.answer || data.error || 'Sorry, an error occurred.');
  } catch(e) {
    thinking.remove();
    addMessage('ai', 'Unable to reach Cirrus. Please try again.');
  }
  btn.disabled = false;
}

document.getElementById('chat-input').addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });

async function sendCSMMessage() {
  const input = document.getElementById('csm-input');
  const question = input.value.trim();
  if (!question) return;
  const msgs = document.getElementById('csm-messages');
  const userMsg = document.createElement('div');
  userMsg.className = 'msg msg-user';
  userMsg.textContent = question;
  msgs.appendChild(userMsg);
  input.value = '';
  const thinking = document.createElement('div');
  thinking.className = 'msg msg-thinking';
  thinking.textContent = 'Cirrus CSM analyzing...';
  msgs.appendChild(thinking);
  msgs.scrollTop = msgs.scrollHeight;
  try {
    const res = await fetch(WORKER_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ question: '[INTERNAL CSM MODE] ' + question }) });
    const data = await res.json();
    thinking.remove();
    const aiMsg = document.createElement('div');
    aiMsg.className = 'msg msg-ai';
    aiMsg.innerHTML = formatMarkdown(data.answer || 'Error.');
    msgs.appendChild(aiMsg);
    msgs.scrollTop = msgs.scrollHeight;
  } catch(e) { thinking.remove(); }
}

document.getElementById('csm-input').addEventListener('keydown', e => { if (e.key === 'Enter') sendCSMMessage(); });

function aiOppCard(tag, name, desc, price, url) {
  return '<a class="ai-opp-card" href="' + url + '" target="_blank"><div class="ai-opp-tag">' + tag + '</div><div class="ai-opp-name">' + name + '</div><div class="ai-opp-desc">' + desc + '</div><span class="ai-opp-price">' + price + '</span></a>';
}

function calculateCost() {
  const visitors = parseInt(document.getElementById('calc-visitors').value) || 50000;
  const type = document.getElementById('calc-type').value;
  const situation = document.getElementById('calc-situation').value;
  const storage = parseFloat(document.getElementById('calc-storage').value) || 0;
  let lines = [], total = 0;

  // Plan
  let plan = 'Pro', planCost = 20;
  if (type === 'ecom' || type === 'saas' || visitors > 500000) { plan = 'Business'; planCost = 200; }
  if (visitors > 2000000) { plan = 'Enterprise'; planCost = 0; }
  lines.push({ label: 'Cloudflare ' + plan + ' Plan', cost: planCost > 0 ? planCost : 'Custom' });
  if (planCost > 0) total += planCost;

  // Workers
  if (type === 'saas' || type === 'api') {
    const wc = 5 + Math.max(0, (visitors * 10 / 1000000 - 10) * 0.5);
    lines.push({ label: 'Workers (serverless compute)', cost: Math.round(wc) });
    total += Math.round(wc);
  }

  // R2
  if (storage > 0) {
    const r2 = storage * 0.015;
    lines.push({ label: 'R2 Storage (' + storage + ' GB)', cost: r2.toFixed(2) });
    total += r2;
  }

  // Argo
  if (type === 'ecom' || type === 'media') {
    const argo = 5 + (visitors / 10000) * 0.1;
    lines.push({ label: 'Argo Smart Routing', cost: Math.round(argo) });
    total += Math.round(argo);
  }

  // Bot Management for ecom
  if (type === 'ecom') {
    lines.push({ label: 'Bot Management (recommended)', cost: '~15' });
    total += 15;
  }

  // Workers AI estimate
  if (type === 'saas' || type === 'api' || type === 'ecom') {
    const neurons = Math.round(visitors * 0.002);
    const aiCost = Math.max(0, (neurons - 10000) * 0.011 / 1000);
    if (aiCost > 0) {
      lines.push({ label: 'Workers AI (~' + neurons + 'K neurons)', cost: aiCost.toFixed(2) });
      total += aiCost;
    } else {
      lines.push({ label: 'Workers AI', cost: 'Free tier' });
    }
  }

  let saving = 0;
  if (situation === 'new') saving = Math.round(total * 0.35);
  if (situation === 'free') saving = Math.round(total * 0.25);

  document.getElementById('result-total').textContent = '$' + Math.round(total) + '/month';
  document.getElementById('result-lines').innerHTML =
    lines.map(l => '<div class="result-line">' + l.label + ' <span>' + (typeof l.cost === 'number' ? '$' + l.cost : l.cost) + '/mo</span></div>').join('') +
    (saving > 0 ? '<div class="result-line" style="color:#4ade80;border:none;margin-top:8px;">Estimated savings vs current setup <span style="color:#4ade80;">-$' + saving + '/mo</span></div>' : '');

  // AI Opportunities
  const cards = [];
  cards.push(aiOppCard('AI GATEWAY', 'AI Gateway', 'Proxy all AI calls — logging, caching, rate limiting, any provider.', 'Free', 'https://developers.cloudflare.com/ai-gateway/'));
  cards.push(aiOppCard('VECTORIZE', 'Vectorize', 'Vector DB for RAG pipelines — 30M dimensions free, natively integrated.', 'Free tier', 'https://developers.cloudflare.com/vectorize/'));
  if (type === 'ecom') {
    cards.push(aiOppCard('WORKERS AI', 'AI Recommendations', 'Run Llama or Qwen3 at the edge for real-time product recommendations.', '$0.011/1K neurons', 'https://ai.cloudflare.com/'));
    cards.push(aiOppCard('AI SEARCH', 'AI Search', 'Natural language product search — connect your catalog, zero infra.', 'Free tier', 'https://developers.cloudflare.com/ai-search/'));
  }
  if (type === 'saas' || type === 'api') {
    cards.push(aiOppCard('AGENTS SDK', 'Cloudflare Agents', 'Autonomous AI agents with persistent memory, tools and scheduling.', 'Included in Workers', 'https://developers.cloudflare.com/agents/'));
    cards.push(aiOppCard('DURABLE OBJECTS', 'Durable Objects', 'Stateful serverless — perfect for agent memory and real-time sessions.', '$0.15/M req', 'https://developers.cloudflare.com/durable-objects/'));
    cards.push(aiOppCard('WORKFLOWS', 'Workflows', 'Durable multi-step AI pipelines that survive failures and retries.', 'Included in Workers', 'https://developers.cloudflare.com/workflows/'));
  }
  if (type === 'media') {
    cards.push(aiOppCard('WORKERS AI', 'FLUX Image Generation', 'Generate images at the edge with FLUX — pay per CPU time, not wall time.', '$0.011/1K neurons', 'https://ai.cloudflare.com/'));
    cards.push(aiOppCard('R2 STORAGE', 'R2 for Media', 'S3-compatible storage with ZERO egress fees — ideal for media assets.', '$0.015/GB/mo', 'https://www.cloudflare.com/products/r2/'));
  }
  if (type === 'blog') {
    cards.push(aiOppCard('AI SEARCH', 'AI Search (Beta)', 'Semantic search for your blog — connect your site URL, free tier available.', 'Free tier', 'https://developers.cloudflare.com/ai-search/'));
    cards.push(aiOppCard('AUTO RAG', 'AutoRAG', 'Auto-build RAG from your content — upload docs, get instant search.', 'Included', 'https://developers.cloudflare.com/autorag/'));
  }
  document.getElementById('ai-opps-grid').innerHTML = cards.join('');

  document.getElementById('calc-result').classList.add('show');
  document.getElementById('cirrus-plan-result').classList.remove('show');
  document.getElementById('cirrus-plan-result').innerHTML = '';
}

function askCirrusPlan() {
  const visitors = document.getElementById('calc-visitors').value || '50000';
  const type = document.getElementById('calc-type').value;
  const situation = document.getElementById('calc-situation').value;
  const storage = document.getElementById('calc-storage').value || '0';
  const typeLabels = { blog: 'Blog/Showcase', ecom: 'E-commerce', saas: 'SaaS/Web app', media: 'Media/Video', api: 'API/Developer' };
  const sitLabels = { new: 'not yet on Cloudflare', free: 'on Cloudflare Free', pro: 'on Cloudflare Pro', business: 'on Cloudflare Business' };
  const msg = 'I have a ' + (typeLabels[type] || type) + ' site with ' + visitors + ' monthly visitors, ' + storage + ' GB storage, currently ' + (sitLabels[situation] || situation) + '. What is the ideal Cloudflare AI strategy for me? Which products should I adopt first, and what are the biggest quick wins?';
  showSection('agent');
  const input = document.getElementById('chat-input');
  if (input) { input.value = msg; setTimeout(sendMessage, 200); }
}

function scoreStatus(val) {
  if (val < 65) return '<div class="score-status critical">Critical</div>';
  if (val < 85) return '<div class="score-status needs-work">Needs work</div>';
  return '<div class="score-status sgreen">Good</div>';
}

function auditGapRow(icon, name, desc, price, urgency) {
  const badge = urgency === 'critical' ? '<span class="badge-critical">CRITICAL</span>' : '<span class="badge-rec">RECOMMENDED</span>';
  return '<div class="audit-gap-row"><div class="audit-gap-icon">' + icon + '</div><div class="audit-gap-content"><div class="audit-gap-name">' + name + '</div><div class="audit-gap-desc">' + desc + '</div><div class="audit-gap-meta">' + badge + '<span class="audit-price-tag">' + price + '</span></div></div></div>';
}

function auditPerfRow(icon, name, improvement, price) {
  return '<div class="audit-gap-row"><div class="audit-gap-icon">' + icon + '</div><div class="audit-gap-content"><div class="audit-gap-name">' + name + '</div><div class="audit-gap-meta"><span class="audit-badge-green">' + improvement + '</span><span class="audit-price-tag">' + price + '</span></div></div></div>';
}

async function runAudit() {
  const url = document.getElementById('audit-url').value.trim();
  const issues = document.getElementById('audit-issues').value;
  if (!url) { alert('Enter a URL'); return; }

  const perfBase = Math.floor(Math.random() * 22) + 49;
  const secBase  = Math.floor(Math.random() * 18) + 53;
  const availBase = Math.floor(Math.random() * 10) + 83;
  const scores = [
    { label: 'Performance', val: perfBase },
    { label: 'Security',    val: secBase  },
    { label: 'Availability', val: availBase }
  ];

  document.getElementById('score-grid').innerHTML = scores.map(s => {
    const cls       = s.val >= 85 ? 'good' : s.val >= 65 ? 'mid' : 'bad';
    const borderCls = s.val >= 85 ? 'good-border' : s.val >= 65 ? 'mid-border' : 'bad-border';
    return '<div class="score-card ' + borderCls + '"><div class="score-val ' + cls + '">' + s.val + '</div><div class="score-label">' + s.label + '</div>' + scoreStatus(s.val) + '</div>';
  }).join('');

  const planCost = (issues === 'security') ? 200 : 20;
  const planName = (planCost === 200) ? 'Business' : 'Pro';
  const totalCost = planCost + 5;
  const safeUrl = url.replace(/'/g, '');

  let html = '<div class="audit-result-grid">';

  // Site header card
  html += '<div class="audit-block"><div class="audit-site-header">';
  html += '<div style="width:32px;height:32px;border-radius:8px;background:var(--orange-dim);display:flex;align-items:center;justify-content:center;color:var(--orange);font-size:16px;">&#127760;</div>';
  html += '<div style="flex:1;min-width:0;"><div style="font-size:13px;font-weight:600;color:rgba(255,255,255,0.9);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">' + url + '</div><div class="audit-summary-line" id="cirrus-summary-line">Cirrus is analyzing...</div></div>';
  html += '<span class="audit-not-cf" id="cf-status-badge">Checking...</span></div></div>';

  // Security card
  html += '<div class="audit-block audit-block-security">';
  html += '<div class="audit-block-hd"><div class="audit-block-icon" style="background:rgba(248,113,113,0.12);color:#f87171;">&#128737;</div><div><div class="audit-block-title">Security Gaps Detected</div><div class="audit-block-subtitle">Critical issues leaving your site exposed</div></div></div>';
  html += '<div class="audit-block-body">';
  html += auditGapRow('&#9888;&#65039;', 'WAF — Web Application Firewall', 'No filtering against SQLi, XSS, OWASP Top 10 attacks. Every request reaches your origin unprotected.', '$20/mo (Pro)', 'critical');
  html += auditGapRow('&#129302;', 'Bot Management', 'Credential stuffing and scraping go undetected. ML-based detection stops fake traffic at the edge.', '$200/mo (Business)', 'critical');
  html += auditGapRow('&#128737;', 'DDoS Protection', 'No unmetered DDoS mitigation. Cloudflare absorbs 321 Tbps+ network attacks automatically.', 'Free on all plans', 'critical');
  html += auditGapRow('&#128065;&#65039;', 'Page Shield', 'Third-party scripts can inject malicious code (supply chain attacks) without detection.', '$200/mo (Business)', 'recommended');
  html += '</div></div>';

  // Performance card
  html += '<div class="audit-block audit-block-perf">';
  html += '<div class="audit-block-hd"><div class="audit-block-icon" style="background:var(--orange-dim);color:var(--orange);">&#128200;</div><div><div class="audit-block-title">Performance Improvements</div><div class="audit-block-subtitle">Expected gains after Cloudflare activation</div></div></div>';
  html += '<div class="audit-block-body">';
  html += auditPerfRow('&#9917;&#65039;', 'Global CDN (330+ datacenters)', '-40 to 60% load time via edge caching', 'Free');
  html += auditPerfRow('&#9889;', 'Argo Smart Routing', '~30% faster via intelligent path optimization', '$5/mo + $0.10/GB');
  html += auditPerfRow('&#128247;', 'Image Optimization (Polish)', '-20 to 35% image weight, auto WebP', 'Pro+');
  html += auditPerfRow('&#9201;&#65039;', 'Waiting Room', 'Traffic spike protection — no more 503 errors', 'Business+');
  html += '</div></div>';

  // AI Opportunities card
  html += '<div class="audit-block audit-block-ai">';
  html += '<div class="audit-block-hd"><div class="audit-block-icon" style="background:rgba(139,92,246,0.15);color:#a78bfa;">&#10024;</div><div><div class="audit-block-title">AI Platform Opportunities</div><div class="audit-block-subtitle">Edge AI products you can activate today</div></div></div>';
  html += '<div class="audit-block-body"><div class="audit-ai-grid">';
  html += aiOppCard('AI GATEWAY', 'AI Gateway', 'Proxy all AI calls — logging, caching, rate limiting. Works with any provider.', 'Free', 'https://developers.cloudflare.com/ai-gateway/');
  html += aiOppCard('WORKERS AI', 'Workers AI', '50+ open-source models at the edge. Pay for CPU time only — up to 10x cheaper than cloud.', '$0.011/1K neurons', 'https://ai.cloudflare.com/');
  html += aiOppCard('AI SEARCH', 'AI Search (Beta)', 'Semantic natural language search — connect your site URL, zero infrastructure needed.', 'Free tier', 'https://developers.cloudflare.com/ai-search/');
  html += aiOppCard('VECTORIZE', 'Vectorize', 'Vector DB for RAG pipelines. 30M dimensions free, natively integrated with Workers AI.', 'Free tier', 'https://developers.cloudflare.com/vectorize/');
  html += '</div></div></div>';

  // Cost summary card
  html += '<div class="audit-block audit-block-cost">';
  html += '<div class="audit-block-hd"><div class="audit-block-icon" style="background:rgba(74,222,128,0.1);color:#4ade80;">&#128176;</div><div><div class="audit-block-title">Cost Summary</div><div class="audit-block-subtitle">Estimated monthly investment</div></div></div>';
  html += '<div class="audit-block-body">';
  html += '<div class="audit-cost-row"><span style="font-size:13px;color:rgba(255,255,255,0.8);">Cloudflare ' + planName + ' Plan</span><span class="audit-price-tag">$' + planCost + '/mo</span></div>';
  html += '<div class="audit-cost-row"><span style="font-size:13px;color:rgba(255,255,255,0.8);">Argo Smart Routing</span><span class="audit-price-tag">$5/mo base</span></div>';
  html += '<div class="audit-cost-row"><span style="font-size:13px;color:rgba(255,255,255,0.8);">CDN + DDoS + SSL</span><span class="audit-price-tag">Free</span></div>';
  html += '<div class="audit-cost-row"><span style="font-size:13px;color:rgba(255,255,255,0.8);">AI Gateway + AI Search</span><span class="audit-price-tag">Free tier</span></div>';
  html += '</div>';
  html += '<div class="audit-cost-total"><span class="audit-total-label">Total estimate</span><span class="audit-total-amount">$' + totalCost + '/month</span></div>';
  html += '</div>';

  html += '</div>'; // end audit-result-grid
  html += '<button class="audit-deeper-btn" onclick="askDeeperAnalysis(\\'' + safeUrl + '\\', \\'' + issues + '\\')">&#128172; Ask Cirrus for a deeper analysis</button>';

  document.getElementById('audit-cards').innerHTML = html;
  document.getElementById('audit-result').classList.add('show');

  // Async: fetch AI summary and update site header
  try {
    const user = getOrCreateUserId();
    const res = await fetch(WORKER_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question: 'Perform a detailed Cloudflare audit for ' + url + '. Issue: ' + issues + '. Provide: 1) Is it on Cloudflare? 2) Top 3 critical security gaps with exact product names and prices 3) Top 3 performance improvements with percentages 4) AI opportunities specific to this site type 5) Exact total monthly cost. Be specific and actionable.',
        userId: user.id, userName: user.name
      })
    });
    const data = await res.json();
    const answer = data.answer || '';
    const isOnCF = /already.{0,40}cloudflare|on cloudflare|using cloudflare|protected by cloudflare/i.test(answer);
    const summaryEl = document.getElementById('cirrus-summary-line');
    const cfBadge   = document.getElementById('cf-status-badge');
    if (summaryEl) summaryEl.textContent = (answer.split('\\n').find(l => l.trim().length > 20) || 'Analysis complete.').slice(0, 130);
    if (cfBadge) {
      cfBadge.textContent = isOnCF ? 'On Cloudflare' : 'Not on Cloudflare';
      if (isOnCF) { cfBadge.style.color = '#4ade80'; cfBadge.style.background = 'rgba(74,222,128,0.1)'; cfBadge.style.borderColor = 'rgba(74,222,128,0.25)'; }
    }
  } catch(e) {
    const summaryEl = document.getElementById('cirrus-summary-line');
    if (summaryEl) summaryEl.textContent = 'Analysis complete.';
  }
}

function askDeeperAnalysis(url, issue) {
  const issueLabels = { speed: 'slow speed and loading time', security: 'security vulnerabilities and attacks', cost: 'high bandwidth costs', downtime: 'downtime and availability issues', all: 'a full optimization' };
  const msg = 'Can you give me a deeper analysis and recommendations for ' + url + '? The main issue is ' + (issueLabels[issue] || issue) + '.';
  showSection('agent');
  const input = document.getElementById('chat-input');
  if (input) { input.value = msg; setTimeout(sendMessage, 200); }
}

async function loadNews() {
  const wrap = document.getElementById('news-wrap');
  wrap.innerHTML = '<div class="news-loading">Loading Cloudflare news in real time...</div>';
  try {
    const res = await fetch(WORKER_URL, { method: 'GET' });
    const data = await res.json();
    const news = data.news || [];
    wrap.innerHTML = news.map(n => {
      const date = n.pubDate ? new Date(n.pubDate).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }) : 'Recent';
      const title = n.title || '';
      const desc = (n.description || '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&amp;/g, '&').replace(/<[^>]*>/g, '').trim().slice(0, 180);
      const link = n.link || '#';
      return '<a href="' + link + '" target="_blank" style="text-decoration:none;"><div class="news-card"><span class="news-source">' + (n.source || '') + '</span><div class="news-content"><div class="news-title">' + title + '</div><div class="news-desc">' + desc + '</div><div class="news-date">' + date + ' &nbsp;&#8599;</div></div></div></a>';
    }).join('');
  } catch(e) { wrap.innerHTML = '<div class="news-loading">Unable to load news.</div>'; }
}

async function loadTicker() {
  try {
    const res = await fetch(WORKER_URL, { method: 'GET' });
    const data = await res.json();
    const news = data.news || [];
    const sep = '  ·  ';
    const items = news.map(n => n.title || '').filter(Boolean);
    const trail = '<strong>Cirrus</strong> powered by Cloudflare Workers AI';
    const content = items.join(sep) + sep + trail;
    const el = document.getElementById('ticker-text');
    if (el) el.innerHTML = content;
    const track = document.getElementById('ticker-track');
    if (track) {
      const duration = Math.max(30, items.length * 8);
      track.style.animationDuration = duration + 's';
    }
  } catch(e) {
    const el = document.getElementById('ticker-text');
    if (el) el.innerHTML = '<strong>Cirrus</strong> powered by Cloudflare Workers AI';
  }
}

const cirrusBubbles = {
  produits: "Need help choosing the right product? Just ask!",
  calculateur: "Want a precise estimate? Describe your setup!",
  audit: "Drop your URL — I will analyze it in seconds 🔍",
  actualites: "Ask me about any of these updates!"
};
function updateCirrusCorner(sectionName) {
  const corner = document.getElementById('cirrus-corner');
  if (!corner) return;
  if (sectionName === 'agent' || sectionName === 'csm') {
    corner.classList.remove('visible');
  } else {
    corner.querySelector('.cirrus-bubble').innerHTML = cirrusBubbles[sectionName] || '';
    corner.classList.add('visible');
  }
}

window.addEventListener('popstate', function() {
  const hash = window.location.hash.replace('#', '') || 'agent';
  const valid = ['agent','produits','calculateur','audit','actualites'];
  showSection(valid.includes(hash) ? hash : 'agent');
});

const sections = ['agent','produits','calculateur','audit','actualites','csm'];
const initHash = window.location.hash.replace('#', '');
if (window.location.search.includes('csm-cirrus-internal') || initHash === 'csm-cirrus-internal') { showSection('csm'); }
else if (sections.includes(initHash)) { showSection(initHash); }
else { showSection('agent'); }
initChat();
loadTicker();
</script>
<div class="cirrus-corner" id="cirrus-corner">
  <div class="cirrus-bubble"></div>
  __CIRRUS__
</div>
</body>
</html>'''

html = html.replace('__CIRRUS__', CIRRUS_SVG)

path = '/Users/haflabghiel/focuseffect-agent/public/index.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! File written:', len(html), 'chars')
