import os
import re

directory = './'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

footer_services_old = re.compile(
    r'<ul class=\"space-y-2\">\s*<li><a[^>]*href=\"#\"[^>]*>Strategy</a></li>\s*<li><a[^>]*href=\"#\"[^>]*>Editorial</a></li>\s*<li><a[^>]*href=\"#\"[^>]*>Identity</a></li>\s*</ul>',
    re.IGNORECASE
)

footer_services_fallback = re.compile(
    r'>Strategy</a></li>\s*<li>[^<]*<a[^>]*>Editorial</a></li>\s*<li>[^<]*<a[^>]*>Identity</a></li>',
    re.IGNORECASE
)

footer_services_new = '''<ul class="space-y-2">
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/luxury-fashion-brands.html">Luxury Fashion</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/designer-boutiques.html">Designer Boutiques</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/bespoke-tailoring.html">Bespoke Tailoring</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/couture-wedding-wear.html">Couture & Wedding</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/premium-ethnic-wear.html">Premium Ethnic Wear</a></li>
        </ul>'''

footer_services_new_fallback = '>Luxury Fashion</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/designer-boutiques.html">Designer Boutiques</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/bespoke-tailoring.html">Bespoke Tailoring</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/couture-wedding-wear.html">Couture & Wedding</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/premium-ethnic-wear.html">Premium Ethnic Wear</a></li>'

for f in files:
    filepath = os.path.join(directory, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Footer replacements
    content = footer_services_old.sub(footer_services_new, content)
    content = footer_services_fallback.sub(footer_services_new_fallback, content)

    if f == 'index.html':
        content = content.replace('<section class="py-24 bg-primary overflow-hidden">', '<section class="py-24 bg-surface-container-low overflow-hidden">')
        content = content.replace('<div class="text-white text-center md:text-left mt-8 max-w-2xl px-2">', '<div class="text-primary text-center md:text-left mt-8 max-w-2xl px-2">')

    # Image fixes
    content = content.replace('young-woman-with-her-beautiful-wedding-dress.jpg', 'woman-robe-siitng-armchair-looking-wedding-dress-wall.jpg')
    content = content.replace('two-young-women-working-clothing-store (1).jpg', 'two-young-women-working-clothing-store.jpg')
    content = content.replace('two-young-women-working-clothing-store%20(1).jpg', 'two-young-women-working-clothing-store.jpg')
    content = content.replace('good-teamwork-is-key-success (1).jpg', 'good-teamwork-is-key-success.jpg')
    content = content.replace('good-teamwork-is-key-success%20(1).jpg', 'good-teamwork-is-key-success.jpg')

    # Spacing fixes
    content = content.replace('py-48', 'py-16')
    content = content.replace('pb-32', 'pb-12')
    content = content.replace('mb-32', 'mb-12')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Processed {f}")

# Rename images
public_dir = './public'
if os.path.exists(public_dir):
    for img in os.listdir(public_dir):
        if '(1)' in img or '%20(1)' in img:
            old_path = os.path.join(public_dir, img)
            new_name = img.replace(' (1)', '').replace('%20(1)', '')
            new_path = os.path.join(public_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {img} to {new_name}")
