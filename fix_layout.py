import os
import re
import glob

# 1. Fix about.html padding
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

if '<main>' in about_content:
    about_content = about_content.replace('<main>', '<main class="pt-28 md:pt-36 pb-12">')
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(about_content)
    print("Fixed about.html padding")

# 2. Fix service pages grid break
service_pages = [
    'luxury-fashion-brands.html',
    'designer-boutiques.html',
    'bespoke-tailoring.html',
    'couture-wedding-wear.html',
    'premium-ethnic-wear.html'
]

for page in service_pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We look for the exact pattern where `</div>` immediately precedes the `<p class="... mt-8">`
        # Because we erroneously inserted it AFTER the `</div>`
        pattern = r'(</a>\s*)</div>(\s*<p class="text-on-surface-variant text-lg leading-relaxed font-light mt-8">.*?We also.*?</p>)'
        
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            # Move the </div> AFTER the <p>
            new_content = re.sub(pattern, r'\1\2\n      </div>', content, flags=re.DOTALL | re.IGNORECASE)
            with open(page, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed grid Layout in {page}")
        elif 'We also' in content:
            # Let's try an alternative pattern if the above fails
            pattern2 = r'(</a>\s*)</div>(\s*<p class="text-on-surface-variant[^>]*>.*?We also.*?</p>)'
            
            if re.search(pattern2, content, re.DOTALL | re.IGNORECASE):
                new_content = re.sub(pattern2, r'\1\2\n      </div>', content, flags=re.DOTALL | re.IGNORECASE)
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed grid Layout in {page} (alt)")
            else:
                # One more try for premium-ethnic-wear since it uses "Our expertise also extends"
                pattern3 = r'(</a>\s*)</div>(\s*<p class="text-on-surface-variant[^>]*>.*?(We also|Our expertise also).*?</p>)'
                if re.search(pattern3, content, re.DOTALL | re.IGNORECASE):
                    new_content = re.sub(pattern3, r'\1\2\n      </div>', content, flags=re.DOTALL | re.IGNORECASE)
                    with open(page, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed grid Layout in {page} (alt 2)")

print("Done fixing layout!")
