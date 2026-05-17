import os
import glob
import re

directory = "/Users/atharvalepse/Downloads/Luxora-main"
html_files = glob.glob(os.path.join(directory, "*.html"))

pattern = re.compile(r'(<li>\s*<a[^>]+href="/privacy-policy\.html"[^>]*>Privacy Policy</a>\s*</li>)', re.IGNORECASE)

for file in html_files:
    if file.endswith('terms-and-conditions.html'):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '/terms-and-conditions.html' not in content:
        match = pattern.search(content)
        if match:
            matched_str = match.group(1)
            new_link = matched_str.replace('/privacy-policy.html', '/terms-and-conditions.html').replace('Privacy Policy', 'Terms &amp; Conditions')
            new_content = content.replace(matched_str, matched_str + '\n          ' + new_link)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer in {file}")

# Update contact.html with form footer
contact_file = os.path.join(directory, "contact.html")
with open(contact_file, 'r', encoding='utf-8') as f:
    contact_content = f.read()

form_footer = '''          </iframe>
          <p class="text-center text-xs text-stone-500 mt-4">
            By submitting this form, you agree to our <a href="/terms-and-conditions.html" class="underline hover:text-[#D4AF37]">Terms &amp; Conditions</a> and <a href="/privacy-policy.html" class="underline hover:text-[#D4AF37]">Privacy Policy</a>.
          </p>'''

if 'By submitting this form' not in contact_content:
    contact_content = contact_content.replace('          </iframe>', form_footer)
    with open(contact_file, 'w', encoding='utf-8') as f:
        f.write(contact_content)
    print("Updated form footer in contact.html")
