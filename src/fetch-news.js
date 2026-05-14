// Récupère les dernières actualités Cloudflare en temps réel
export async function fetchCloudflareNews() {
  const news = [];

  try {
    // Blog officiel Cloudflare
    const blogRes = await fetch("https://blog.cloudflare.com/rss");
    const blogXml = await blogRes.text();
    const blogItems = parseRSS(blogXml, 5);
    news.push(...blogItems.map(i => ({ ...i, source: "Cloudflare Blog" })));
  } catch (e) {
    news.push({ title: "Blog Cloudflare indisponible", source: "Cloudflare Blog" });
  }

  try {
    // Changelog officiel Cloudflare (nouveaux produits et mises à jour)
    const changelogRes = await fetch("https://developers.cloudflare.com/changelog/rss.xml");
    const changelogXml = await changelogRes.text();
    const changelogItems = parseRSS(changelogXml, 5);
    news.push(...changelogItems.map(i => ({ ...i, source: "Cloudflare Changelog" })));
  } catch (e) {
    news.push({ title: "Changelog Cloudflare indisponible", source: "Cloudflare Changelog" });
  }

  return news;
}

// Parse un flux RSS et retourne les N premiers articles
function parseRSS(xml, limit = 5) {
  const items = [];
  const itemRegex = /<item>([\s\S]*?)<\/item>/g;
  let match;

  while ((match = itemRegex.exec(xml)) !== null && items.length < limit) {
    const item = match[1];
    const title = extractTag(item, "title");
    const link = extractTag(item, "link");
    const pubDate = extractTag(item, "pubDate");
    const description = extractTag(item, "description")
      ?.replace(/<[^>]*>/g, "")
      ?.slice(0, 200);

    if (title) {
      items.push({ title, link, pubDate, description });
    }
  }

  return items;
}

function extractTag(xml, tag) {
  const match = xml.match(new RegExp(`<${tag}[^>]*><!\\[CDATA\\[([\\s\\S]*?)\\]\\]></${tag}>|<${tag}[^>]*>([\\s\\S]*?)</${tag}>`));
  return match ? (match[1] || match[2])?.trim() : null;
}