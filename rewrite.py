import re

with open('premium-ethnic-wear.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace metas
html = html.replace('Premium Ethnic Wear Marketing | Luxora', 'Couture & Wedding Wear Marketing | Luxora')
html = html.replace('Specialist digital marketing for premium ethnic wear brands. Elevate heritage fashion with targeted SEO, e-commerce strategy, and global storytelling.', 'Luxury digital marketing for couture and wedding wear labels. Connect with high-net-worth clients for bridal fashion.')

# Hero
html = html.replace('/women-shopping-buying-consumer-products-customer-day-celebration.jpg', '/woman-robe-siitng-armchair-looking-wedding-dress-wall.jpg')
html = html.replace('Premium ethnic wear editorial', 'Luxury Bridal Couture')
html = html.replace('Digital Marketing for Heritage Fashion', 'Digital Excellence for Custom Luxury')
html = html.replace('Where <span class="italic font-normal text-[#D4AF37]">Ancient Craft</span> Meets Modern Digital Prestige', 'Couture <span class="italic font-normal text-[#D4AF37]">&amp;</span> Wedding Wear')
html = html.replace('LUXORA is the specialist digital marketing agency for premium ethnic wear brands. We honour the artisanal heritage of Indian and South Asian luxury fashion — then build the digital strategies, SEO foundations, and e-commerce experiences that bring your brand to the world\'s most discerning buyers.', 'The world\'s most discerning brides and couture collectors aren\'t just looking for a garment — they\'re searching for an artisan who can transform a dream into a masterpiece. Luxora ensures that artisan is you.')
html = html.replace('Premium ethnic wear represents one of the fastest-growing segments in luxury fashion. <a href="/about" class="text-[#D4AF37] hover:underline font-bold transition-colors">About Luxora</a> - we have been positioned at the intersection of cultural prestige and digital performance since 2018.', 'Wedding wear marketing requires a balance of romance and precision. We don\'t just run ads; we build digital experiences that mirror the intimacy and sophistication of your bridal salon or couture studio.')

# Stats in hero
html = html.replace('Ethnic Wear Brands Scaled', 'Luxury Fashion Partners')
html = html.replace('4.2×', '300%')
html = html.replace('Average ROAS Delivered', 'Qualified Lead Increase')
html = html.replace('18+', '98%')
html = html.replace('Global Markets Reached', 'Client Retention Rate')
html = html.replace('96%', '15+')
html = html.replace('Client Retention Rate', 'Years Combined Experience')

# Approach section
html = html.replace('Artisanal Heritage Deserves a <span class="italic">Prestige</span> Digital Platform', 'The Digital Atelier <span class="italic">Strategy</span>')

html = html.replace('Premium ethnic wear is more than fashion — it is woven memory, generational craft, and cultural identity expressed in silk, zari, and thread. Your brand carries stories that mass-market fashion simply cannot replicate. The challenge is ensuring the digital world understands that difference.', '<b>Aspirational SEO:</b> Dominating search for high-intent bridal and couture terms while maintaining an air of exclusivity.')

html = html.replace('Most digital agencies treat ethnic wear like any other apparel vertical. They apply generic SEO tactics and run templated ad campaigns that strip the soul from your brand. LUXORA does the opposite. We study your craft, your weave, your clientele — and then build a digital ecosystem that elevates your heritage rather than erasing it.', '<b>Pinterest Dominance:</b> Curating visual storylines that capture the \'mood-board\' phase of the luxury bridal journey.')

html = html.replace('From bridal lehenga collections to premium saree labels, from hand-block-printed kurta brands to couture sherwani houses, we have the deep sector knowledge and creative precision to market premium ethnic fashion at the level it deserves — to buyers in India, the UK, the US, the UAE, and beyond.', '<b>High-Net-Worth Targeting:</b> Precise digital placement seen only by the clients who value — and afford — your bespoke creations.')

html = html.replace('Our expertise also extends to <a href="/designer-boutiques" class="underline hover:text-[#D4AF37] transition-colors font-semibold">designer boutique marketing</a> and <a href="/luxury-fashion-brands" class="underline hover:text-[#D4AF37] transition-colors font-semibold">luxury fashion brand services</a> for labels at every stage of their premium journey.', 'Our expertise also extends to <a href="/bespoke-tailoring" class="underline hover:text-[#D4AF37] transition-colors font-semibold">bespoke tailoring</a> and <a href="/luxury-fashion-brands" class="underline hover:text-[#D4AF37] transition-colors font-semibold">luxury fashion brand services</a> for labels at every stage of their premium journey.')

html = html.replace('/fashion-expert-worker-selecting-variety-trendy-items-client.jpg', '/medium-shot-brazilian-woman-working-as-clothing-designer.jpg')
html = html.replace('Fashion expert selecting premium ethnic wear', 'Designer at Work')
html = html.replace('"Curating the finest in heritage fashion."', '"Market the Immeasurable."')

# Services
html = html.replace('Digital Marketing Built for Premium Ethnic Wear Brands', 'Designing for the Aspirational')
html = html.replace('Every service is calibrated to the unique demands of heritage fashion — protecting cultural authenticity while driving measurable commercial growth.', 'Digital brand audits and visual refinement services ensuring your online presence matches the craftsmanship of your atelier.')

# Let's replace the services titles and text
html = html.replace('Ethnic Fashion SEO &amp; Keyword Strategy', 'Heritage SEO')
html = html.replace('We research and target the high-intent search terms your ideal customer uses — "bridal lehenga online," "luxury sarees India," and hundreds of long-tail variations.', 'Positioning your brand as a heritage house of tomorrow, ensuring visibility for traditional and contemporary couture searches globally.')

html = html.replace('Luxury Heritage Brand Storytelling', 'Editorial Storytelling')
html = html.replace('Every stitch has a story. We craft compelling brand narratives that articulate your craft heritage, design philosophy, and artisanal process in ways that resonate deeply with premium buyers.', 'We transform your lookbooks into digital narratives, using editorial-grade copy and strategic UI/UX to create an online \'appointment\' experience.')

html = html.replace('Premium E-Commerce Strategy &amp; Optimisation', 'Exclusive PPC')
html = html.replace('We design and optimise product pages, category structures, and checkout flows that mirror the thoughtful experience of visiting your atelier in person. Combined with strategic remarketing, your e-commerce store becomes your most powerful sales channel.', 'Paid media strategies that respect price point and prestige, appearing only in environments where luxury decision-makers reside.')

html = html.replace('Paid Media for Affluent &amp; Bridal Audiences', 'Bridal &amp; Couture Media Buying')
html = html.replace('Precision paid campaigns targeting bridal shoppers, NRI audiences, and high-income fashion buyers across India, UK, USA, UAE, Canada, and Australia.', 'White-listed ad placements, gate-kept content strategies, and high-intent keyword targeting. We ensure your brand isn\'t seen by everyone, but by everyone who matters.')

html = html.replace('Social Media &amp; Influencer Marketing', 'Hyper-Local Luxury Targeting')
html = html.replace('We manage your social channels with editorial discipline — each post intentionally composed to build aspiration, showcase craftsmanship, and grow an engaged community of genuine buyers.', 'We specialize in Hyper-Local Luxury SEO, ensuring you dominate premium searches within your city and surrounding driving-distance affluent postcodes.')

html = html.replace('Bridal &amp; Festive Season Campaign Marketing', 'Visual &amp; Creative Direction')
html = html.replace('We build dedicated seasonal campaign strategies targeting wedding season, Diwali, Eid, and Navratri, driving early consideration and confirmed orders well ahead of your competition.', 'While our primary focus is digital strategy and performance, we act as creative directors for your shoots, ensuring every visual aligns with digital platform best practices for luxury brands.')

# Section The Luxora Method
# No changes needed for titles/text really, they are general enough, let's just leave them or tweak
html = html.replace('Premium ethnic wear demands a marketing approach as considered as the craft itself.', 'Couture demands a marketing approach as considered as the craft itself.')
html = html.replace('premium ethnic wear', 'couture &amp; wedding wear')

# The marquee text
html = html.replace('Luxury Ethnic Wear SEO', 'Couture SEO Strategy')
html = html.replace('Indian Bridal Fashion Marketing', 'Luxury Bridal Marketing')
html = html.replace('Premium Saree Brand Strategy', 'Bespoke Dress Marketing')
html = html.replace('NRI Audience Targeting', 'High-Net-Worth Targeting')
html = html.replace('Lehenga Brand Digital Marketing', 'Atelier Brand Agency')
html = html.replace('Heritage Textile Brand Agency', 'Couture Fashion SEO')
html = html.replace('Ethnic Fashion E-Commerce', 'bridal Fashion E-Commerce')

# "Who We Work With"
html = html.replace('From bridal couture houses to ready-to-wear ethnic labels, our expertise spans the full spectrum of premium South Asian and heritage fashion.', 'From bridal couture houses to bespoke bridal designers, our expertise spans the full spectrum of luxury ceremonial styling.')

html = html.replace('Bridal Lehenga Labels', 'Bridal Salons')
html = html.replace('Targeting engaged couples and families planning weddings with high-intent bridal search campaigns.', 'Targeting engaged couples and families planning weddings with high-intent bridal search campaigns.')

html = html.replace('Premium Saree Brands', 'Made-to-Measure Brides')
html = html.replace('Positioning handloom, Banarasi, Kanjeevaram, and designer sarees in front of connoisseurs and gift buyers.', 'Positioning bespoke bridal gowns and designer dresses in front of connoisseurs.')

html = html.replace('Couture Sherwani Houses', 'Groom Attire &amp; Suiting')
html = html.replace('Building groom-side brand awareness and seasonal campaign strategies for wedding and ceremonial wear.', 'Building groom-side brand awareness and seasonal campaign strategies for wedding and ceremonial wear.')

html = html.replace('Ethnic Fusion &amp; Pret', 'Luxury Bridesmaid Labels')
html = html.replace('Scaling premium ready-to-wear collections with social-first strategies and influencer partnerships.', 'Scaling premium ready-to-wear collections with social-first strategies and influencer partnerships.')

html = html.replace('Heritage Textile Brands', 'High-End Bridal Boutiques')
html = html.replace('Communicating craft stories, weave traditions, and artisan-made values to culturally aware luxury buyers.', 'Communicating craft stories and designer lineage to culturally aware luxury buyers.')

# Image Breaker
html = html.replace('two-young-women-working-clothing-store.jpg', 'young-stylish-sexy-woman-pink-luxury-dress-summer-trend-chic-style-fashion-designer-working-office-computer.jpg')
html = html.replace('Women working in a premium clothing store', 'Luxury Marketing Studio')

# CTA section
html = html.replace('one of our premium ethnic fashion specialists', 'one of our couture fashion specialists')

with open('couture-wedding-wear.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
