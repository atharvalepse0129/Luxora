const fs = require('fs');
const path = require('path');

const dir = './';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const footerServicesOld = `<ul class="space-y-2">
          <li><a
              class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]"
              href="#">Strategy</a></li>
          <li><a
              class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]"
              href="#">Editorial</a></li>
          <li><a
              class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]"
              href="#">Identity</a></li>
        </ul>`;

const footerServicesNew = `<ul class="space-y-2">
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/luxury-fashion-brands.html">Luxury Fashion</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/designer-boutiques.html">Designer Boutiques</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/bespoke-tailoring.html">Bespoke Tailoring</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/couture-wedding-wear.html">Couture & Wedding</a></li>
          <li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/premium-ethnic-wear.html">Premium Ethnic Wear</a></li>
        </ul>`;

files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  // Fix footer services links
  // We use a regex that matches the ul class space-y-2 under Services in the footer
  const footerServicesRegex = /<ul class="space-y-2">\s*<li><a[^>]*href="#"[^>]*>Strategy<\/a><\/li>\s*<li><a[^>]*href="#"[^>]*>Editorial<\/a><\/li>\s*<li><a[^>]*href="#"[^>]*>Identity<\/a><\/li>\s*<\/ul>/i;
  content = content.replace(footerServicesRegex, footerServicesNew);
  
  // Alternative fallback if white space is different
  content = content.replace(/>Strategy<\/a><\/li>\s*<li>[^<]*<a[^>]*>Editorial<\/a><\/li>\s*<li>[^<]*<a[^>]*>Identity<\/a><\/li>/gi, 
                            '>Luxury Fashion</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/designer-boutiques.html">Designer Boutiques</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/bespoke-tailoring.html">Bespoke Tailoring</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/couture-wedding-wear.html">Couture & Wedding</a></li><li><a class="text-stone-400 dark:text-zinc-500 hover:text-amber-700 dark:hover:text-amber-500 transition-all font-sans uppercase tracking-[0.15em] text-[10px]" href="/premium-ethnic-wear.html">Premium Ethnic Wear</a></li>');

  // Index specific fixes
  if (file === 'index.html') {
    // Background offwhite for video section
    content = content.replace(/<section class="py-24 bg-primary overflow-hidden">/g, '<section class="py-24 bg-surface-container-low overflow-hidden">');
    content = content.replace(/<div class="text-white text-center md:text-left mt-8 max-w-2xl px-2">/g, '<div class="text-primary text-center md:text-left mt-8 max-w-2xl px-2">');
  }

  // Broken image fixes
  content = content.replace(/young-woman-with-her-beautiful-wedding-dress\.jpg/g, 'woman-robe-siitng-armchair-looking-wedding-dress-wall.jpg');
  content = content.replace(/two-young-women-working-clothing-store \(1\)\.jpg/g, 'two-young-women-working-clothing-store.jpg');
  content = content.replace(/two-young-women-working-clothing-store%20\(1\)\.jpg/g, 'two-young-women-working-clothing-store.jpg');
  content = content.replace(/good-teamwork-is-key-success \(1\)\.jpg/g, 'good-teamwork-is-key-success.jpg');
  content = content.replace(/good-teamwork-is-key-success%20\(1\)\.jpg/g, 'good-teamwork-is-key-success.jpg');

  // Fix padding to reduce negative space (maybe bottom elements had big pb or h-screen applied)
  content = content.replace(/py-48/g, 'py-16');
  content = content.replace(/pb-32/g, 'pb-12');
  content = content.replace(/mb-32/g, 'mb-12');
  
  content = content.replace(/h-\[100dvh\] overflow-y-auto w-full/g, 'h-[100dvh] overflow-y-auto w-[80%]'); // This was in fix_ios
  
  // Some pages had "min-h-[100dvh]" which can cause issues with padding. Let's make sure section paddings are balanced.
  
  fs.writeFileSync(filePath, content, 'utf8');
});

console.log('Fixed links, background, and broken image src. Moving on to rename images.');

// Rename images in public
const publicDir = './public';
if (fs.existsSync(publicDir)) {
  const images = fs.readdirSync(publicDir);
  images.forEach(img => {
    if (img.includes('(1)')) {
      const oldPath = path.join(publicDir, img);
      const newPath = path.join(publicDir, img.replace(' (1)', '').replace('%20(1)', ''));
      fs.renameSync(oldPath, newPath);
      console.log(`Renamed ${img} to ${path.basename(newPath)}`);
    }
  });
}
