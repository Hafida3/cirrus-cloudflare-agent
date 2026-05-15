const DOCS = [
  { url: 'https://developers.cloudflare.com/workers-ai/llms-full.txt',  product: 'workers-ai', title: 'Workers AI' },
  { url: 'https://developers.cloudflare.com/ai-gateway/llms-full.txt',  product: 'ai-gateway', title: 'AI Gateway' },
  { url: 'https://developers.cloudflare.com/vectorize/llms-full.txt',   product: 'vectorize',  title: 'Vectorize' },
  { url: 'https://developers.cloudflare.com/kv/llms-full.txt',          product: 'kv',         title: 'Workers KV' },
  { url: 'https://developers.cloudflare.com/workers/llms-full.txt',     product: 'workers',    title: 'Cloudflare Workers' },
  { url: 'https://developers.cloudflare.com/pages/llms-full.txt',       product: 'pages',      title: 'Cloudflare Pages' },
];

const CHUNK_WORDS   = 500;
const EMBED_BATCH   = 25;   // texts per Workers AI call
const INSERT_BATCH  = 500;  // vectors per Vectorize insert call

function chunkText(text) {
  const words = text.split(/\s+/).filter(Boolean);
  const chunks = [];
  for (let i = 0; i < words.length; i += CHUNK_WORDS) {
    chunks.push(words.slice(i, i + CHUNK_WORDS).join(' '));
  }
  return chunks;
}

export async function handleIngest(request, env) {
  const secret = request.headers.get('X-Ingest-Secret');
  if (!secret || secret !== env.INGEST_SECRET) {
    return new Response('Unauthorized', { status: 401 });
  }

  const results = [];

  const { searchParams } = new URL(request.url);
  const productFilter = searchParams.get('product');
  const docs = productFilter ? DOCS.filter(d => d.product === productFilter) : DOCS;

  for (const doc of docs) {
    try {
      const resp = await fetch(doc.url);
      if (!resp.ok) {
        results.push({ product: doc.product, error: `fetch failed: ${resp.status}` });
        continue;
      }

      const text = await resp.text();
      const chunks = chunkText(text);
      const vectors = [];

      for (let i = 0; i < chunks.length; i += EMBED_BATCH) {
        const batch = chunks.slice(i, i + EMBED_BATCH);
        const embedResult = await env.AI.run('@cf/baai/bge-base-en-v1.5', { text: batch });

        for (let j = 0; j < batch.length; j++) {
          vectors.push({
            id: `${doc.product}-${i + j}`,
            values: embedResult.data[j],
            metadata: {
              url: doc.url,
              title: doc.title,
              product: doc.product,
              text: batch[j].slice(0, 1500),
            },
          });
        }
      }

      for (let i = 0; i < vectors.length; i += INSERT_BATCH) {
        await env.VECTORIZE.insert(vectors.slice(i, i + INSERT_BATCH));
      }

      results.push({ product: doc.product, chunks: chunks.length, vectors: vectors.length });
    } catch (err) {
      results.push({ product: doc.product, error: err.message });
    }
  }

  return new Response(JSON.stringify({ ok: true, results }, null, 2), {
    headers: { 'Content-Type': 'application/json' },
  });
}

export default {
  async fetch(request, env) {
    const { pathname } = new URL(request.url);
    if (request.method === 'GET' && pathname === '/ingest') {
      return handleIngest(request, env);
    }
    return new Response('Not found', { status: 404 });
  },
};
