const fs = require('fs');
const glob = require('glob'); // Not required if we just array files

const files = [
    'index.html',
    'about.html',
    'contact.html',
    'bespoke-tailoring.html',
    'couture-wedding-wear.html',
    'designer-boutiques.html',
    'luxury-fashion-brands.html',
    'premium-ethnic-wear.html',
    'case-studies.html',
    'privacy-policy.html',
    'blog.html'
];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');

        // 1. Viewport fit cover
        content = content.replace(
            /<meta content="width=device-width, initial-scale=1\.0" name="viewport">/g,
            '<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport">'
        );
        content = content.replace(
            /<meta name="viewport" content="width=device-width, initial-scale=1\.0">/g,
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
        );

        // 2. iOS Header spacing & mobile menu alignment
        // Add safe area padding to nav
        content = content.replace(
            /<nav\s+class="fixed top-0 w-full z-50 bg-white\/90 dark:bg-zinc-950\/90 backdrop-blur-xl border-b border-stone-200 dark:border-zinc-800 transition-all duration-300">/g,
            '<nav class="fixed top-0 w-full z-50 bg-white/90 dark:bg-zinc-950/90 backdrop-blur-xl border-b border-stone-200 dark:border-zinc-800 transition-all duration-300" style="padding-top: env(safe-area-inset-top); padding-left: env(safe-area-inset-left); padding-right: env(safe-area-inset-right);">'
        );
        
        // Fix mobile menu right align and iOS h-dvh
        content = content.replace(
            /<div id="mobile-menu" class="hidden fixed inset-0 bg-white dark:bg-zinc-950 z-50 transform translate-x-full transition-transform duration-500 ease-in-out flex flex-col pt-32 px-6 h-screen overflow-y-auto w-full">/g,
            '<div id="mobile-menu" class="hidden fixed inset-0 bg-white dark:bg-zinc-950 z-50 transform translate-x-full transition-transform duration-500 ease-in-out flex flex-col pt-32 px-6 h-[100dvh] overflow-y-auto w-full" style="padding-top: calc(8rem + env(safe-area-inset-top)); padding-bottom: env(safe-area-inset-bottom);">'
        );
        
        // Right align text in mobile menu
        content = content.replace(
            /<div class="flex flex-col space-y-8 pb-12">[\s\S]*?<a class="font-serif italic text-3xl text-\[#D4AF37\] border-b border-stone-200 dark:border-zinc-800 pb-4" href="\/">Home<\/a>/g,
            '<div class="flex flex-col space-y-8 pb-12 text-right">\n        <a class="font-serif italic text-3xl text-[#D4AF37] border-b border-stone-200 dark:border-zinc-800 pb-4 block w-full" href="/">Home</a>'
        );
        content = content.replace(
            /<a class="font-serif italic text-3xl text-\[#D4AF37\] border-b border-stone-200 dark:border-zinc-800 pb-4" href="\/about\.html">About<\/a>/g,
            '<a class="font-serif italic text-3xl text-[#D4AF37] border-b border-stone-200 dark:border-zinc-800 pb-4 block w-full" href="/about.html">About</a>'
        );
        content = content.replace(
            /<div class="text-\[#D4AF37\] font-serif italic text-3xl border-b border-stone-200 dark:border-zinc-800 pb-4">/g,
            '<div class="text-[#D4AF37] font-serif italic text-3xl border-b border-stone-200 dark:border-zinc-800 pb-4 block w-full">'
        );
        content = content.replace(
            /mt-6 font-sans text-sm not-italic opacity-90 pl-4 border-l-2 border-\[#D4AF37\]\/30/g,
            'mt-6 font-sans text-sm not-italic opacity-90 pr-4 border-r-2 border-[#D4AF37]/30 text-right'
        );
        
        fs.writeFileSync(file, content, 'utf8');
        console.log('Processed', file);
    }
});
