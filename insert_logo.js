const fs = require('fs');
const cheerio = require('cheerio');

const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));

for (const file of files) {
  const content = fs.readFileSync(file, 'utf-8');
  const $ = cheerio.load(content);
  
  // Header Logo Replacement
  $('nav > a').each(function() {
    const text = $(this).text().trim();
    if (text === 'LUXORA') {
      $(this).removeClass('font-serif text-2xl tracking-[0.2em] uppercase text-black dark:text-white');
      $(this).addClass('flex items-center transition-opacity hover:opacity-80');
      $(this).html('<img src="/logo.png" alt="Luxora Digital Marketing" class="h-10 md:h-12 w-auto object-contain">');
    }
  });

  // Footer Logo Replacement (Bonus UI/UX consistency)
  $('footer a.font-serif.italic').each(function() {
    const text = $(this).text().trim().toLowerCase();
    if (text === 'luxora') {
      $(this).removeClass('font-serif italic text-xl lowercase text-stone-900 dark:text-stone-100');
      $(this).addClass('flex items-center transition-opacity hover:opacity-80 mb-6 md:mb-8 block max-w-fit');
      $(this).html('<img src="/logo.png" alt="Luxora Digital Marketing" class="h-10 w-auto object-contain grayscale opacity-70 hover:grayscale-0 hover:opacity-100 transition-all duration-500">');
    }
  });

  fs.writeFileSync(file, $.html());
}

console.log('Logo successfully inserted into all pages.');
