import os
import re

link_class = 'class="underline hover:text-[#D4AF37] transition-colors font-semibold"'

def apply_about():
    with open('about.html', 'r', encoding='utf-8') as f: content = f.read()
    
    s1 = f'<p class="mt-4">Luxora exists as a partner solely for brands operating at the top tier of human desire. Our <a href="/luxury-fashion-brands.html" {link_class}>luxury fashion brand marketing services</a> are engineered for labels that refuse to be ordinary.</p>'
    content = content.replace('<div class="font-body text-on-surface-variant text-lg leading-relaxed max-w-4xl space-y-6">', '<div class="font-body text-on-surface-variant text-lg leading-relaxed max-w-4xl space-y-6">\n  ' + s1)
    
    s2 = f'<p class="mt-4">Whether we\'re working with <a href="/designer-boutiques.html" {link_class}>designer boutiques</a> or positioning <a href="/bespoke-tailoring.html" {link_class}>bespoke and couture labels</a> for global audiences, our process remains the same: Beauty, Position, Transform.</p>'
    content = re.sub(r'(<ul class="list-disc pl-5 space-y-2">.*?</ul>)', r'\1\n  ' + s2, content, flags=re.DOTALL)
    
    s3 = f'<p class="text-on-surface-variant text-lg font-light mb-8 max-w-2xl text-center mx-auto">If your brand is ready for the next tier, <a href="/contact.html" {link_class}>request a strategy session</a> to begin.</p>'
    content = re.sub(r'Let Us Show You Exactly How to Get There.\s*</h2>', 'Let Us Show You Exactly How to Get There.</h2>\n  ' + s3, content)
    
    with open('about.html', 'w', encoding='utf-8') as f: f.write(content)

def apply_contact():
    with open('contact.html', 'r', encoding='utf-8') as f: content = f.read()
    
    s1 = f'<p class="mt-4 text-on-surface-variant text-base">We prioritise <a href="/luxury-fashion-brands.html" {link_class}>luxury fashion brands</a> with a clear heritage and commitment to craftsmanship. Not sure if you qualify? <a href="/about.html" {link_class}>Learn about our methodology</a> and the brands we serve.</p>'
    content = re.sub(r'(<h3 class="text-2xl font-light mb-4 italic">The Selection Criteria</h3>\s*<p[^>]*>.*?</p>)', r'\1\n            ' + s1, content, flags=re.DOTALL)
    
    s2 = f'<p class="mt-4 text-on-surface-variant text-lg font-light">To explore <a href="/index.html" {link_class}>our full range of services</a>, visit our homepage.</p>'
    content = re.sub(r'(<h1[^>]*>.*?</h1>\s*<p[^>]*>.*?</p>)', r'\1\n      ' + s2, content, flags=re.DOTALL)
    
    with open('contact.html', 'w', encoding='utf-8') as f: f.write(content)

def apply_service(filename, s1, s2, s3):
    with open(filename, 'r', encoding='utf-8') as f: content = f.read()
    
    # In the intro paragraph
    content = re.sub(r'(<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl">.*?</p>)', r'\1\n      ' + s1, content, flags=re.DOTALL)
    
    # In related services / body copy (append to Our Approach)
    content = re.sub(r'(<span class="inline-block transition-transform group-hover:translate-x-2">→</span>\s*</a>\s*</div>)', r'\1\n      ' + s2, content, flags=re.DOTALL)
    
    # CTA section body text
    content = re.sub(r'(Ready to Grow Your Brand Globally\?</span>\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>)', r'\1\n    ' + s3, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f: f.write(content)

# Define snippets
lfb_s1 = f'<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl mt-4">Our luxury fashion brand marketing system is built exclusively for premium men\'s and women\'s clothing labels. <a href="/about.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">Learn about our agency</a> and the philosophy behind our approach.</p>'
lfb_s2 = f'<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">We also specialise in growth strategies for <a href="/designer-boutiques.html" {link_class}>designer boutiques</a>, <a href="/bespoke-tailoring.html" {link_class}>bespoke tailoring brands</a>, and <a href="/couture-wedding-wear.html" {link_class}>couture and bridal designers</a>.</p>'
lfb_s3 = f'<p class="text-white/70 text-lg md:text-xl font-light leading-relaxed mb-10 max-w-2xl mx-auto">Ready to elevate your label? <a href="/contact.html" {link_class}>Apply to work with us</a> for a private strategy session.</p>'

db_s1 = f'<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl mt-4">Our designer boutique marketing system is part of our broader <a href="/luxury-fashion-brands.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">luxury fashion brand marketing</a> suite. <a href="/about.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">Discover how Luxora works</a> before applying.</p>'
db_s2 = f'<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">We also help <a href="/premium-ethnic-wear.html" {link_class}>premium ethnic wear labels</a> reach affluent global audiences with the same precision approach.</p>'
db_s3 = f'<p class="text-white/70 text-lg md:text-xl font-light leading-relaxed mb-10 max-w-2xl mx-auto"><a href="/contact.html" {link_class}>Start your strategy session</a> and let us show you exactly how to grow your boutique.</p>'

bt_s1 = f'<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl mt-4">Bespoke tailoring occupies a unique intersection of craft and luxury. Our <a href="/luxury-fashion-brands.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">luxury fashion brand marketing</a> expertise means we understand how to position your craft at the pinnacle of menswear.</p>'
bt_s2 = f'<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">Our work extends across related sectors including <a href="/couture-wedding-wear.html" {link_class}>couture and wedding wear marketing</a> where the standards of precision and prestige are equally demanding.</p>'
bt_s3 = f'<p class="text-white/70 text-lg md:text-xl font-light leading-relaxed mb-10 max-w-2xl mx-auto">Speak to our team and <a href="/contact.html" {link_class}>request a consultation</a> today.</p>'

cw_s1 = f'<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl mt-4">Couture and bridal fashion demands a marketing partner that understands desirability. Our <a href="/luxury-fashion-brands.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">luxury fashion marketing agency</a> works exclusively with premium labels. <a href="/about.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">Our brand philosophy</a> reflects the same commitment to excellence your clients expect.</p>'
cw_s2 = f'<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">We also work with <a href="/bespoke-tailoring.html" {link_class}>bespoke tailoring marketing</a> - a natural companion sector where craftsmanship and exclusivity converge.</p>'
cw_s3 = f'<p class="text-white/70 text-lg md:text-xl font-light leading-relaxed mb-10 max-w-2xl mx-auto"><a href="/contact.html" {link_class}>Apply for a private session</a> to discuss how we can position your couture label for global recognition.</p>'

pew_s1 = f'<p class="text-white/80 text-lg md:text-xl leading-relaxed font-light mb-10 max-w-2xl mt-4">Premium ethnic wear represents one of the fastest-growing segments in luxury fashion. <a href="/about.html" class="text-[#D4AF37] hover:underline font-bold transition-colors">About Luxora</a> - we have been positioned at the intersection of cultural prestige and digital performance since 2018.</p>'
pew_s2 = f'<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">Our expertise also extends to <a href="/designer-boutiques.html" {link_class}>designer boutique marketing</a> and <a href="/luxury-fashion-brands.html" {link_class}>luxury fashion brand services</a> for labels at every stage of their premium journey.</p>'
pew_s3 = f'<p class="text-white/70 text-lg md:text-xl font-light leading-relaxed mb-10 max-w-2xl mx-auto">Take the first step - <a href="/contact.html" {link_class}>start a strategy session</a> with Luxora today.</p>'

# Execute
apply_about()
apply_contact()

apply_service('luxury-fashion-brands.html', lfb_s1, lfb_s2, lfb_s3)
apply_service('designer-boutiques.html', db_s1, db_s2, db_s3)
apply_service('bespoke-tailoring.html', bt_s1, bt_s2, bt_s3)
apply_service('couture-wedding-wear.html', cw_s1, cw_s2, cw_s3)
apply_service('premium-ethnic-wear.html', pew_s1, pew_s2, pew_s3)

print("Linked subpages successfully.")
