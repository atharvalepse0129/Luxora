const fs = require('fs');
const cheerio = require('cheerio');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'services.html');

const dropdownHTML = `
<div class="relative group">
  <button class="text-[#D4AF37] hover:opacity-80 font-serif italic text-2xl tracking-tight transition-all duration-300 flex items-center gap-1 focus:outline-none">
    Services
    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
    </svg>
  </button>
  <div class="absolute left-0 mt-8 w-72 bg-white/95 dark:bg-zinc-950/95 backdrop-blur-xl border border-stone-200 dark:border-zinc-800 shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col py-4 z-50 rounded-sm">
    <a href="/luxury-fashion-brands.html" class="px-6 py-3 font-sans text-xs uppercase tracking-widest text-[#D4AF37] hover:bg-stone-100 dark:hover:bg-zinc-900 transition-colors">Luxury Fashion</a>
    <a href="/designer-boutiques.html" class="px-6 py-3 font-sans text-xs uppercase tracking-widest text-[#D4AF37] hover:bg-stone-100 dark:hover:bg-zinc-900 transition-colors">Designer Boutiques</a>
    <a href="/bespoke-tailoring.html" class="px-6 py-3 font-sans text-xs uppercase tracking-widest text-[#D4AF37] hover:bg-stone-100 dark:hover:bg-zinc-900 transition-colors">Bespoke Tailoring</a>
    <a href="/couture-wedding-wear.html" class="px-6 py-3 font-sans text-xs uppercase tracking-widest text-[#D4AF37] hover:bg-stone-100 dark:hover:bg-zinc-900 transition-colors">Couture & Wedding Wear</a>
    <a href="/premium-ethnic-wear.html" class="px-6 py-3 font-sans text-xs uppercase tracking-widest text-[#D4AF37] hover:bg-stone-100 dark:hover:bg-zinc-900 transition-colors">Premium Ethnic Wear</a>
  </div>
</div>
`;

files.forEach(file => {
    const filePath = path.join(dir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const $ = cheerio.load(content);
    let changed = false;

    // Find the Services link
    const servicesLink = $('nav a[href="/services.html"]');
    
    if (servicesLink.length > 0) {
        servicesLink.replaceWith(dropdownHTML);
        changed = true;
    }

    if (changed) {
        fs.writeFileSync(filePath, $.html());
        console.log(`Updated nav in ${file}`);
    }
});

// Remove services.html
const servicesFile = path.join(dir, 'services.html');
if (fs.existsSync(servicesFile)) {
    fs.unlinkSync(servicesFile);
    console.log('Removed services.html');
}

console.log('Dropdown replacement complete.');
