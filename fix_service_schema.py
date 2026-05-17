import os

service_pages = ['luxury-fashion-brands.html', 'designer-boutiques.html', 'bespoke-tailoring.html', 'couture-wedding-wear.html', 'premium-ethnic-wear.html']

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

for fname in service_pages:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script type="application/ld+json">' not in content:
        content = content.replace('</head>', service_schema + '\n</head>')
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added schema to {fname}")
