import re

# Read the template from premium-ethnic-wear.html
with open('premium-ethnic-wear.html', 'r', encoding='utf-8') as f:
    template = f.read()

# We need to replace text and images that are specific to premium-ethnic-wear with couture-wedding-wear
replacements = {
    "Premium Ethnic Wear Marketing | Luxora": "Couture & Wedding Wear Marketing | Luxora",
    '<meta name="description" content="Specialist digital marketing for premium ethnic wear brands. Elevate heritage fashion with targeted SEO, e-commerce strategy, and global storytelling.">': '<meta name="description" content="Luxury digital marketing for couture and wedding wear labels. Connect with high-net-worth clients for bridal fashion.">',
    "Specialist digital marketing for premium ethnic wear brands. Elevate heritage fashion with targeted SEO, e-commerce strategy, and global storytelling.": "Luxury digital marketing for couture and wedding wear labels. Connect with high-net-worth clients for bridal fashion.",
    
    # Hero Section
    "/women-shopping-buying-consumer-products-customer-day-celebration.jpg": "/woman-robe-siitng-armchair-looking-wedding-dress-wall.jpg",
    "Premium ethnic wear editorial": "Luxury Bridal Couture",
    "Digital Marketing for Heritage Fashion": "Digital Excellence for Custom Luxury",
    "Where <span class=\"italic font-normal text-[#D4AF37]\">Ancient Craft</span> Meets Modern Digital Prestige": "Couture <span class=\"italic font-normal text-[#D4AF37]\">&amp;</span> Wedding Wear",
    "LUXORA is the specialist digital marketing agency for premium ethnic wear brands. We honour the artisanal heritage of Indian and South Asian luxury fashion — then build the digital strategies, SEO foundations, and e-commerce experiences that bring your brand to the world's most discerning buyers.": "The world's most discerning brides and couture collectors aren't just looking for a garment — they're searching for an artisan who can transform a dream into a masterpiece. Luxora ensures that artisan is you.",
    "Premium ethnic wear represents one of the fastest-growing segments in luxury fashion. <a href=\"/about\" class=\"text-[#D4AF37] hover:underline font-bold transition-colors\">About Luxora</a> - we have been positioned at the intersection of cultural prestige and digital performance since 2018.": "Wedding wear marketing requires a balance of romance and precision. We don't just run ads; we build digital experiences that mirror the intimacy and sophistication of your bridal salon or couture studio.",
    
    "15+": "15+",
    "Ethnic Wear Brands Scaled": "Luxury Fashion Partners",
    "4.2×": "300%",
    "Average ROAS Delivered": "Qualified Lead Increase",
    
    # Approach
    "Artisanal Heritage Deserves a <span class=\"italic\">Prestige</span> Digital Platform": "The Digital Atelier <span class=\"italic\">Strategy</span>",
    "Premium ethnic wear is more than fashion — it is woven memory, generational craft, and cultural identity expressed in silk, zari, and thread. Your brand carries stories that mass-market fashion simply cannot replicate. The challenge is ensuring the digital world understands that difference.": "Aspirational SEO: Dominating search for high-intent bridal and couture terms while maintaining an air of exclusivity.",
    "Most digital agencies treat ethnic wear like any other apparel vertical. They apply generic SEO tactics and run templated ad campaigns that strip the soul from your brand. LUXORA does the opposite. We study your craft, your weave, your clientele — and then build a digital ecosystem that elevates your heritage rather than erasing it.": "Pinterest Dominance: Curating visual storylines that capture the 'mood-board' phase of the luxury bridal journey.",
    "From bridal lehenga collections to premium saree labels, from hand-block-printed kurta brands to couture sherwani houses, we have the deep sector knowledge and creative precision to market premium ethnic fashion at the level it deserves — to buyers in India, the UK, the US, the UAE, and beyond.": "High-Net-Worth Targeting: Precise digital placement seen only by the clients who value — and afford — your bespoke creations.",
    "Our expertise also extends to <a href=\"/designer-boutiques\" class=\"underline hover:text-[#D4AF37] transition-colors font-semibold\">designer boutique marketing</a> and <a href=\"/luxury-fashion-brands\" class=\"underline hover:text-[#D4AF37] transition-colors font-semibold\">luxury fashion brand services</a> for labels at every stage of their premium journey.": "Our work extends across related sectors including <a href=\"/bespoke-tailoring\" class=\"underline hover:text-[#D4AF37] transition-colors font-semibold\">bespoke tailoring marketing</a> and <a href=\"/luxury-fashion-brands\" class=\"underline hover:text-[#D4AF37] transition-colors font-semibold\">luxury fashion brand services</a>.",

    "/fashion-expert-worker-selecting-variety-trendy-items-client.jpg": "/medium-shot-brazilian-woman-working-as-clothing-designer.jpg",
    "Fashion expert selecting premium ethnic wear": "Designer at Work",
    '"Curating the finest in heritage fashion."': '"Market the Immeasurable."',
    
    # Services
    "Digital Marketing Built for Premium Ethnic Wear Brands": "Designing for the Aspirational",
    "Every service is calibrated to the unique demands of heritage fashion — protecting cultural authenticity while driving measurable commercial growth.": "Digital brand audits and visual refinement services ensuring your online presence matches the craftsmanship of your atelier.",
    
    # Needs to match all 6 services...
}

# The easiest way is to re-construct couture-wedding-wear using regex on the main sections.
# But template replacement is faster. Let's do a more robust approach:
# Just take the full premium-ethnic-wear HTML, write a custom python script or just do string replacements.

# Let's replace the nav active state:
template = template.replace('href="/premium-ethnic-wear"', 'href="/premium-ethnic-wear.html"')
template = template.replace('href="/couture-wedding-wear"', 'href="/couture-wedding-wear.html"')
# It's an extensionless URL site, so don't add .html
pass

