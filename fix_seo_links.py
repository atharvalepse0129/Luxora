import os
import glob
import re

def clean_html_extensions(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all simple href="/pagename.html" with href="/pagename"
    # We will match href="/(about|contact|luxury-fashion-brands|designer-boutiques|bespoke-tailoring|couture-wedding-wear|premium-ethnic-wear).html"
    pages = [
        'about', 'contact', 'luxury-fashion-brands', 'designer-boutiques',
        'bespoke-tailoring', 'couture-wedding-wear', 'premium-ethnic-wear'
    ]
    
    for page in pages:
        content = re.sub(rf'href="/{page}\.html"', f'href="/{page}"', content)
        content = re.sub(rf'href="https://luxoradigitalmarketing\.com/{page}\.html"', f'href="https://luxoradigitalmarketing.com/{page}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Process HTML files
for html_file in glob.glob('*.html'):
    clean_html_extensions(html_file)

# Process Sitemap
if os.path.exists('public/sitemap.xml'):
    clean_html_extensions('public/sitemap.xml')
    print("Cleaned public/sitemap.xml")

print("Cleaned HTML extensions from internal links!")
