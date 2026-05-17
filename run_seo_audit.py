import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

meta_desc = {
    'index.html': 'Luxora is a luxury fashion marketing agency helping premium clothing brands, designer boutiques, and couture labels grow through precision digital strategy, brand storytelling, and high-ticket client acquisition.',
    'about.html': 'Learn how Luxora\'s luxury brand marketing methodology — built around beauty, positioning, and transformation — helps high-end fashion labels achieve global prestige and sustainable growth.',
    'contact.html': 'Apply for a private strategy session with Luxora. We partner with a limited number of luxury clothing brands each quarter to deliver bespoke digital growth systems.',
    'luxury-fashion-brands.html': 'Luxora\'s luxury fashion brand marketing services for men\'s and women\'s premium labels. Precision targeting, editorial content, and high-ticket conversion systems built exclusively for luxury.',
    'designer-boutiques.html': 'Digital marketing for designer boutiques. Luxora helps high-end boutique owners attract affluent clients, elevate brand positioning, and build long-term customer loyalty.',
    'bespoke-tailoring.html': 'Digital marketing for bespoke tailoring brands. Precision campaigns to attract affluent clientele pursuing custom-made suiting.',
    'couture-wedding-wear.html': 'Luxury digital marketing for couture and wedding wear labels. Connect with high-net-worth clients for bridal fashion.',
    'premium-ethnic-wear.html': 'Specialist digital marketing for premium ethnic wear brands. Elevate heritage fashion with targeted SEO, e-commerce strategy, and global storytelling.',
    'blog.html': 'Explore the latest insights on luxury fashion marketing from the experts at Luxora.',
    'privacy-policy.html': 'Privacy policy for Luxora digital marketing agency.',
    'case-studies.html': 'View client case studies and results achieved by Luxora, the premium fashion marketing agency.'
}

titles = {
    'index.html': 'Luxury Fashion Marketing Agency | Luxora',
    'about.html': 'About Luxora | Luxury Brand Digital Marketing Agency',
    'contact.html': 'Contact Luxora | Request a Strategy Session',
    'luxury-fashion-brands.html': 'Luxury Fashion Brand Marketing | Luxora',
    'designer-boutiques.html': 'Designer Boutique Marketing Agency | Luxora',
    'bespoke-tailoring.html': 'Bespoke Tailoring Brand Marketing | Luxora',
    'couture-wedding-wear.html': 'Couture & Wedding Wear Marketing | Luxora',
    'premium-ethnic-wear.html': 'Premium Ethnic Wear Marketing | Luxora',
    'case-studies.html': 'Case Studies | Luxora',
    'blog.html': 'Insights & Articles | Luxora',
    'privacy-policy.html': 'Privacy Policy | Luxora'
}

org_schema = """<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Organization",
 "name": "Luxora",
 "url": "https://luxoradigitalmarketing.com",
 "logo": "https://luxoradigitalmarketing.com/logo.png",
 "description": "Luxury fashion brand marketing agency specialising in premium clothing labels, designer boutiques, and couture brands.",
 "telephone": "+19843749646",
 "email": "contact@luxoradigitalmarketing.com",
 "address": {
   "@type": "PostalAddress",
   "addressLocality": "London"
 },
 "sameAs": []
}
</script>"""

service_schema = """<script type="application/ld+json">
{
 "@context": "https://schema.org",
 "@type": "Service",
 "serviceType": "Digital Marketing for Luxury Fashion Brands",
 "provider": {
   "@type": "Organization",
   "name": "Luxora",
   "url": "https://luxoradigitalmarketing.com"
 },
 "areaServed": "Worldwide",
 "description": "Precision digital marketing services for luxury clothing brands including client acquisition, brand storytelling, and high-ticket conversion architecture.",
 "offers": {
   "@type": "AggregateOffer",
   "lowPrice": "1700",
   "highPrice": "4500",
   "priceCurrency": "USD"
 }
}
</script>"""

about_old = '''<p class="font-body text-on-surface-variant text-lg leading-relaxed max-w-4xl">
                        Luxora is a luxury brand digital marketing firm, which exists as a brand house and solely with the brands that operate in the top tier of human desire. We are not fashionable - we make fashions. Our product will change an emerging brand in the realm of fashion, hospitality, and lifestyle to garner attention, gather cultural impact, and turn desire into holding a long-term loyalty. We have been helping premium brands to do so since 2018.
                    </p>'''

about_new = '''<div class="font-body text-on-surface-variant text-lg leading-relaxed max-w-4xl space-y-6">
  <p>Luxora was founded on a single conviction: luxury fashion brands deserve a marketing partner that understands what luxury actually means.</p>
  <p>Since 2018, we have partnered exclusively with premium clothing labels, designer boutiques, bespoke tailors, and couture houses — helping them attract high-net-worth clients, elevate their brand positioning, and build the kind of desirability that no discount campaign can manufacture.</p>
  <p>Our methodology is built on three pillars:</p>
  <ul class="list-disc pl-5 space-y-2">
    <li><strong class="font-bold text-[#D4AF37]">Beauty</strong> — creating visuals that communicate exclusivity and stop your ideal audience in their scroll.</li>
    <li><strong class="font-bold text-[#D4AF37]">Position</strong> — framing your brand as a cultural authority, not a service provider, in the minds of high-value buyers.</li>
    <li><strong class="font-bold text-[#D4AF37]">Transform</strong> — designing digital experiences that convert desire into loyalty — from the first impression to the lifetime relationship.</li>
  </ul>
  <p>We do not work with mass-market brands. We do not use generic playbooks. Every strategy we build is hand-crafted to reflect the unique heritage, aesthetic, and aspirations of your label — and measured against the metrics that actually matter to a premium business.</p>
</div>'''

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title
    title = titles.get(fname, 'Luxury Fashion Marketing Agency | Luxora')
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content, flags=re.DOTALL)
    
    # Remove existing description if any
    content = re.sub(r'<meta name="description" content="[^"]*">\s*', '', content)
    content = re.sub(r'<meta name="description" content="[^"]*" />\s*', '', content)
    
    # 2. Add Meta Description, Open Graph & Twitter Cards
    desc = meta_desc.get(fname, meta_desc['index.html'])
    meta_tags = f'''<meta name="description" content="{desc}">
<meta property="og:type" content="website" />
<meta property="og:url" content="https://luxoradigitalmarketing.com/" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="https://luxoradigitalmarketing.com/og-image.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:site_name" content="Luxora" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="https://luxoradigitalmarketing.com/og-image.jpg" />'''

    # Insert meta tags after title
    content = re.sub(r'(<title>.*?</title>)', r'\1\n' + meta_tags, content, flags=re.DOTALL)

    # Remove existing schema to prevent duplicates
    content = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', content, flags=re.DOTALL)

    # 3. Add JSON-LD Schema
    schema = org_schema if fname == 'index.html' else service_schema
    # Avoid adding service schema to contact, privacy, about, blog if you want, but the prompt says 
    # "Service Pages (repeat for each)". We can just add Service schema to service pages.
    service_pages = ['luxury-fashion-brands.html', 'designer-boutiques.html', 'bespoke-tailoring.html', 'couture-wedding-wear.html', 'premium-ethnic-wear.html']
    
    if fname == 'index.html':
        content = re.sub(r'</head>', org_schema + '\n</head>', content)
    elif fname in service_pages:
        content = re.sub(r'</head>', service_schema + '\n</head>', content)

    # 4. Replace broken privacy setting in footer
    content = re.sub(r'href="#">Privacy</a>', r'href="/privacy-policy.html">Privacy Policy</a>', content)
    content = re.sub(r'href="#">Privacy Policy</a>', r'href="/privacy-policy.html">Privacy Policy</a>', content)
    
    # 5. Fix Image Alts
    # hero-home-new.jpg
    content = re.sub(r'(<img[^>]*src="/hero-home-new\.jpg"[^>]*)alt="[^"]*"', r'\1alt="Luxury fashion brand marketing — Luxora agency hero"', content)
    if 'alt=' not in content and '/hero-home-new.jpg' in content:
        content = content.replace('src="/hero-home-new.jpg"', 'src="/hero-home-new.jpg" alt="Luxury fashion brand marketing — Luxora agency hero"')
        
    # hero-about.jpg
    content = re.sub(r'(<img[^>]*src="/hero-about\.jpg"[^>]*)alt="[^"]*"', r'\1alt="Luxora luxury brand digital marketing methodology"', content)
    if 'alt=' not in content and '/hero-about.jpg' in content:
        content = content.replace('src="/hero-about.jpg"', 'src="/hero-about.jpg" alt="Luxora luxury brand digital marketing methodology"')
    # Because of data-alt, we can just replace data-alt with alt
    content = content.replace('data-alt="Elegant golden miniature desk ornaments and a modern laptop bathed in a warm sunset glow"', 'alt="Luxora luxury brand digital marketing methodology"')

    # Logo
    content = re.sub(r'alt="Luxora"', r'alt="Luxora — Luxury Fashion Marketing Agency"', content)
    content = re.sub(r'alt="Luxora Logo"', r'alt="Luxora — Luxury Fashion Marketing Agency"', content)
    
    # Specific missing ones: "Sector images" - wait, the user's audit says "Sector images ... lack descriptive alt attributes"
    # Earlier we had:
    # <img alt="Luxury Fashion Brands" ...
    # Let's replace the bare "Luxury Fashion Brands" with "Luxury fashion brands men and women digital marketing" in index.html
    if fname == 'index.html':
        content = content.replace('alt="Luxury Fashion Brands"', 'alt="Luxury fashion brands men and women digital marketing"')
        content = content.replace('alt="Designer Boutiques"', 'alt="Designer boutique marketing and client acquisition"')
        content = content.replace('alt="Bespoke Tailoring"', 'alt="Bespoke tailoring brand marketing agency"')
        content = content.replace('alt="Couture"', 'alt="Couture and wedding wear brand marketing"')
        content = content.replace('alt="Ethnic Wear"', 'alt="Premium ethnic wear brand digital marketing"')

    # 6. About Page Content Rewrite
    if fname == 'about.html':
        # Let's replace the content strictly by finding the old text
        if "Luxora is a luxury brand digital marketing firm, which exists as a brand house" in content:
            # We use a regex to match the paragraph block safely since whitespace might differ
            content = re.sub(r'<p class="[^"]*">\s*Luxora is a luxury brand digital marketing firm.*?</p>', about_new, content, flags=re.DOTALL)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO update complete.")
