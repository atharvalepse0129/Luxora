#!/bin/bash
# Fix nav logos - increase to h-24 md:h-28, remove py-2
for f in index.html about.html services.html contact.html blog.html case-studies.html luxury-fashion-brands.html designer-boutiques.html couture-wedding-wear.html premium-ethnic-wear.html; do
  if [ -f "$f" ]; then
    sed -i '' 's/class="h-16 md:h-20 w-auto object-contain py-2"/class="h-24 md:h-28 w-auto object-contain"/g' "$f"
  fi
done

# Fix footer logos - increase h-10 to h-20
for f in index.html about.html services.html contact.html case-studies.html luxury-fashion-brands.html designer-boutiques.html couture-wedding-wear.html premium-ethnic-wear.html bespoke-tailoring.html; do
  if [ -f "$f" ]; then
    sed -i '' 's/class="h-10 w-auto object-contain"/class="h-20 w-auto object-contain"/g' "$f"
  fi
done

# Fix bespoke-tailoring nav logo
sed -i '' 's/class="h-12 md:h-14 w-auto object-contain"/class="h-24 md:h-28 w-auto object-contain"/g' bespoke-tailoring.html

# Fix blog footer logo
sed -i '' 's/class="w-auto object-contain grayscale opacity-70 hover:grayscale-0 hover:opacity-100 transition-all duration-500 h-16"/class="w-auto object-contain grayscale opacity-70 hover:grayscale-0 hover:opacity-100 transition-all duration-500 h-20"/g' blog.html

echo "All logo sizes updated!"
