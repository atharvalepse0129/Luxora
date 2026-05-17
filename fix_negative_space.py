import os
import re

directory = './'
files = [f for f in os.listdir(directory) if f.endswith('.html')]

# We want to remove excessive vertical margins and paddings across all files
for f in files:
    filepath = os.path.join(directory, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Padding top on main tag which causes the huge white block below navbar
    content = content.replace('<main class="pt-48">', '<main>')
    content = content.replace('<main class="pt-32">', '<main>')
    
    # Or if it's a class string with other classes
    content = re.sub(r'\bpt-48\b', 'pt-20', content)
    content = re.sub(r'\bpt-40\b', 'pt-20', content)
    content = re.sub(r'\bpt-32\b', 'pt-16', content)
    
    content = re.sub(r'\bpy-48\b', 'py-16 md:py-24', content)
    content = re.sub(r'\bpy-40\b', 'py-16 md:py-20', content)
    content = re.sub(r'\bmd:py-40\b', 'md:py-24', content)
    content = re.sub(r'\bpy-32\b', 'py-16', content)
    content = re.sub(r'\bmd:py-32\b', 'md:py-20', content)
    
    content = re.sub(r'\bpy-28\b', 'py-16', content)
    content = re.sub(r'\bmd:py-28\b', 'md:py-20', content)

    content = re.sub(r'\bpb-48\b', 'pb-20', content)
    content = re.sub(r'\bpb-40\b', 'pb-20', content)
    content = re.sub(r'\bpb-32\b', 'pb-16', content)

    content = re.sub(r'\bmb-48\b', 'mb-20', content)
    content = re.sub(r'\bmb-40\b', 'mb-20', content)
    content = re.sub(r'\bmb-32\b', 'mb-16', content)
    
    content = re.sub(r'\bmt-48\b', 'mt-20', content)
    content = re.sub(r'\bmt-40\b', 'mt-20', content)
    content = re.sub(r'\bmt-32\b', 'mt-16', content)

    # In case we over-replaced inside the backdrop or mobile menu
    # Let's fix mobile menu if it got mangled - we want pt-32 or pt-48 for the menu so it's not tucked under nav
    # The mobile menu has: id="mobile-menu"
    # It has a calc(6rem + env(...)) anyway so it's fine.

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Removed negative/excessive space in {f}")
