// Tarifs officiels Cloudflare (mis à jour mai 2026)
export const CLOUDFLARE_PRICING = {
  plans: {
    free: {
      name: "Free",
      price: 0,
      description: "CDN, DNS, SSL, DDoS basic",
      features: ["CDN global", "SSL gratuit", "DDoS protection basique", "3 Page Rules", "Analytics basique"]
    },
    pro: {
      name: "Pro",
      price: 20,
      per: "month/domain",
      description: "Pour sites professionnels",
      features: ["Tout Free +", "WAF managed rules", "Image optimization", "25 Page Rules", "Support prioritaire"]
    },
    business: {
      name: "Business",
      price: 200,
      per: "month/domain",
      description: "Pour e-commerce et apps critiques",
      features: ["Tout Pro +", "Custom WAF rules", "50 Page Rules", "SLA 100% uptime", "PCI compliance"]
    },
    enterprise: {
      name: "Enterprise",
      price: "custom",
      description: "À partir de ~3000$/mois",
      features: ["Tout Business +", "Account manager dédié", "SLA personnalisé", "Custom rules illimités"]
    }
  },
  products: {
    workers: {
      name: "Cloudflare Workers",
      free: "100,000 requêtes/jour",
      paid: "$5/mois + $0.50/million requêtes",
      description: "Code serverless à la périphérie du réseau"
    },
    r2: {
      name: "Cloudflare R2",
      free: "10 GB stockage, 1M opérations Class A",
      paid: "$0.015/GB/mois stockage, $4.50/million opérations write",
      description: "Stockage objet sans frais d'egress"
    },
    stream: {
      name: "Cloudflare Stream",
      paid: "$5/1000 minutes stockées + $1/1000 minutes livrées",
      description: "Hébergement et streaming vidéo"
    },
    pages: {
      name: "Cloudflare Pages",
      free: "Hébergement statique illimité",
      paid: "Inclus dans Workers Paid $5/mois",
      description: "Déploiement de sites statiques et full-stack"
    },
    argo: {
      name: "Argo Smart Routing",
      paid: "$5/mois + $0.10/GB trafic",
      description: "Optimisation des routes réseau, réduit la latence de 30%"
    },
    loadBalancing: {
      name: "Load Balancing",
      paid: "À partir de $5/mois pour 2 origines",
      description: "Répartition de charge et health checks"
    },
    pageShield: {
      name: "Page Shield",
      paid: "Inclus Business+, ou add-on Pro",
      description: "Protection contre les scripts malveillants côté client"
    },
    zaraz: {
      name: "Cloudflare Zaraz",
      free: "Gratuit",
      description: "Gestionnaire de tags tiers via Workers"
    },
    turnstile: {
      name: "Turnstile (CAPTCHA)",
      free: "1M validations/mois gratuites",
      paid: "$0.00030 par validation au-delà",
      description: "Alternative CAPTCHA respectueuse de la vie privée"
    },
    workersAI: {
      name: "Workers AI",
      free: "10,000 neurones/jour gratuits",
      paid: "$0.011 per 1,000 neurons",
      description: "Inférence IA sur le réseau Cloudflare"
    }
  }
};