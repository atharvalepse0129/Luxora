const fs = require('fs');
const cheerio = require('cheerio');
const path = require('path');

const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));

const getHeaderHtml = (activeFile) => `
<nav class="fixed top-0 w-full z-50 bg-white/90 dark:bg-zinc-950/90 backdrop-blur-xl border-b border-stone-200 dark:border-zinc-800 transition-all duration-300">
  <div class="max-w-screen-2xl mx-auto h-24 px-6 md:px-12 flex justify-between items-center">
    <!-- Logo -->
    <a href="/" class="flex-shrink-0 flex items-center transition-transform hover:opacity-80 duration-500">
      <img src="/logo.png" alt="Luxora Digital Marketing" class="h-16 md:h-20 w-auto object-contain py-2">
    </a>

    <!-- Desktop Navigation -->
    <div class="hidden md:flex space-x-10 lg:space-x-14 items-center">
      <a class="${activeFile === 'index.html' ? 'text-stone-900 dark:text-white border-b border-stone-900 dark:border-white pb-1' : 'text-stone-500 dark:text-stone-400 hover:text-amber-700 dark:hover:text-amber-500'} font-serif italic text-2xl tracking-tight transition-all duration-300" href="/">Home</a>
      <a class="${activeFile === 'about.html' ? 'text-stone-900 dark:text-white border-b border-stone-900 dark:border-white pb-1' : 'text-stone-500 dark:text-stone-400 hover:text-amber-700 dark:hover:text-amber-500'} font-serif italic text-2xl tracking-tight transition-all duration-300" href="/about.html">About</a>
      <a class="${activeFile === 'services.html' ? 'text-stone-900 dark:text-white border-b border-stone-900 dark:border-white pb-1' : 'text-stone-500 dark:text-stone-400 hover:text-amber-700 dark:hover:text-amber-500'} font-serif italic text-2xl tracking-tight transition-all duration-300" href="/services.html">Services</a>
      <a class="${activeFile === 'case-studies.html' ? 'text-stone-900 dark:text-white border-b border-stone-900 dark:border-white pb-1' : 'text-stone-500 dark:text-stone-400 hover:text-amber-700 dark:hover:text-amber-500'} font-serif italic text-2xl tracking-tight transition-all duration-300" href="/case-studies.html">Case Studies</a>
      <a class="${activeFile === 'blog.html' ? 'text-stone-900 dark:text-white border-b border-stone-900 dark:border-white pb-1' : 'text-stone-500 dark:text-stone-400 hover:text-amber-700 dark:hover:text-amber-500'} font-serif italic text-2xl tracking-tight transition-all duration-300" href="/blog.html">Blog</a>
    </div>

    <!-- Contact Button -->
    <div class="hidden md:flex items-center">
      <a href="/contact.html" class="bg-black dark:bg-white text-white dark:text-black px-8 py-3.5 text-[11px] font-sans font-bold uppercase tracking-[0.25em] hover:bg-amber-800 dark:hover:bg-amber-200 transition-colors duration-500 shadow-md">Contact Us</a>
    </div>
  </div>
</nav>
`;

for (const file of files) {
  const content = fs.readFileSync(file, 'utf-8');
  const $ = cheerio.load(content);
  
  // Replace the entire <nav> block
  $('nav.fixed.top-0').replaceWith(getHeaderHtml(file));

  // Add padding-top to the first section after the header to account for the larger header (h-24 = 6rem = 96px)
  // Usually the hero section has `h-screen` or `pt-40`. If it's `h-screen`, we don't strictly *need* to change it, 
  // but let's ensure body has no margin/padding bugs.
  
  // Bonus: Let's also make sure footer logo is larger
  $('footer img[src="/logo.png"]').removeClass('h-10').addClass('h-16');

  fs.writeFileSync(file, $.html());
}

console.log('Advanced header successfully injected into all pages.');
