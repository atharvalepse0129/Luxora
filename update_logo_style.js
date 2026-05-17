const fs = require('fs');
const cheerio = require('cheerio');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

files.forEach(file => {
    const filePath = path.join(dir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const $ = cheerio.load(content);
    let changed = false;

    // Header logo replacement
    $('nav img[src="/logo.png"]').each(function() {
        $(this).attr('class', 'w-40 md:w-48 lg:w-56 h-auto object-contain transition-transform duration-500 hover:scale-105 dark:invert dark:hue-rotate-180');
        $(this).removeAttr('style'); // Remove inline styles if any
        changed = true;
    });

    // Footer logo replacement
    $('footer img[src="/logo.png"]').each(function() {
        $(this).attr('class', 'w-32 md:w-40 h-auto object-contain transition-all duration-500 hover:scale-105 dark:invert dark:hue-rotate-180 grayscale hover:grayscale-0');
        $(this).removeAttr('style');
        changed = true;
    });

    // Catch any remaining /logo.png everywhere else (just in case they are outside nav and footer initially)
    $('a[href="/"] img[src="/logo.png"]').each(function() {
        const parentTag = $(this).closest('nav').length > 0 ? 'nav' : ($(this).closest('footer').length > 0 ? 'footer' : 'other');
        if (parentTag === 'other') {
            $(this).attr('class', 'w-40 md:w-48 lg:w-56 h-auto object-contain transition-all duration-500 hover:scale-105 dark:invert dark:hue-rotate-180');
            changed = true;
        }
    });

    if (changed) {
        fs.writeFileSync(filePath, $.html());
        console.log(`Updated ${file}`);
    }
});
console.log('Logo update complete.');
