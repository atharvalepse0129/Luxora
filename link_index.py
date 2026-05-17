import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero intro
old_hero = 'Luxora is the growth engine built exclusively for luxury clothing brands. From bespoke suits and wedding couture\n        to designer boutiques and premium ethnic wear.'
if old_hero not in content:
    # try one-liner
    old_hero = 'Luxora is the growth engine built exclusively for luxury clothing brands. From bespoke suits and wedding couture to designer boutiques and premium ethnic wear.'
new_hero = 'Luxora is the growth engine built exclusively for <a href="/luxury-fashion-brands.html" class="underline hover:text-[#D4AF37] transition-colors">luxury fashion brand marketing</a>, from bespoke suits and wedding couture to <a href="/designer-boutiques.html" class="underline hover:text-[#D4AF37] transition-colors">designer boutiques</a> and <a href="/premium-ethnic-wear.html" class="underline hover:text-[#D4AF37] transition-colors">premium ethnic wear</a>.'
content = content.replace(old_hero, new_hero)
# In case whitespace doesn't match:
import re
content = re.sub(r'Luxora is the growth engine built exclusively for luxury clothing brands.*?premium ethnic wear\.', new_hero, content, flags=re.DOTALL)

# Add to Specialized Sectors
sectors_anchor = '<h2 class="font-headline text-4xl md:text-5xl mb-4">Specialized Sectors We Elevate</h2>'
new_sectors = sectors_anchor + '\n      <p class="font-body text-on-surface-variant text-lg max-w-3xl mb-8 mt-4">We work with <a href="/luxury-fashion-brands.html" class="underline hover:text-secondary transition-colors">luxury fashion brands</a>, <a href="/designer-boutiques.html" class="underline hover:text-secondary transition-colors">designer boutiques</a>, <a href="/bespoke-tailoring.html" class="underline hover:text-secondary transition-colors">bespoke tailoring brands</a>, <a href="/couture-wedding-wear.html" class="underline hover:text-secondary transition-colors">couture and wedding wear</a> designers, and <a href="/premium-ethnic-wear.html" class="underline hover:text-secondary transition-colors">premium ethnic wear</a> labels.</p>'
if '<a href="/luxury-fashion-brands.html" class="underline hover:text-secondary transition-colors">' not in content:
    content = content.replace(sectors_anchor, new_sectors)

# Why Luxora
why_anchor = '<h2 class="font-headline text-4xl md:text-5xl">Why Luxora</h2>'
new_why = why_anchor + '\n        <p class="mt-4 font-body text-on-surface-variant text-lg">Learn more <a href="/about.html" class="underline hover:text-secondary transition-colors">about our approach and philosophy</a> and why luxury brands choose Luxora as their growth partner.</p>'
if '<a href="/about.html" class="underline hover:text-secondary transition-colors">' not in content:
    content = content.replace(why_anchor, new_why)

# Final CTA
cta_anchor = 'Let Us Show You Exactly How to Get There.\n      </h2>'
new_cta = cta_anchor + '\n      <p class="font-body text-lg text-on-surface-variant mb-6 text-center max-w-xl mx-auto">Ready to take your label to the premium tier? <a href="/contact.html" class="underline hover:text-[#D4AF37] transition-colors font-semibold">Apply for a strategy session</a> with our team today.</p>'
if 'Ready to take your label to the premium tier?' not in content:
    content = content.replace(cta_anchor, new_cta)
    # Also handle alternate newline cases
    content = re.sub(r'Let Us Show You Exactly How to Get There.\s*</h2>', 'Let Us Show You Exactly How to Get There.</h2>\n      <p class="font-body text-lg text-on-surface-variant mb-6 text-center max-w-xl mx-auto">Ready to take your label to the premium tier? <a href="/contact.html" class="underline hover:text-[#D4AF37] transition-colors font-semibold">Apply for a strategy session</a> with our team today.</p>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
