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

    // Hide Case Studies and Blog
    $('nav a').each(function() {
        const text = $(this).text().trim();
        if (text === 'Case Studies' || text === 'Blog') {
            $(this).remove();
            changed = true;
        }
    });

    // Make navigation links golden
    $('nav .hidden.md\\:flex.space-x-10 a, nav .hidden.md\\:flex.lg\\:space-x-14 a').each(function() {
        // Remove standard colors, add golden base
        let cls = $(this).attr('class') || '';
        cls = cls.replace(/text-stone-900|dark:text-white|text-stone-500|dark:text-stone-400|border-stone-900/g, '');
        if (cls.includes('border-b')) {
            cls = cls.replace(/dark:border-white/g, '');
            cls += ' text-amber-500 border-amber-500 dark:border-amber-500';
        } else {
            cls += ' text-amber-600 dark:text-amber-500';
        }
        // Normalize spaces
        $(this).attr('class', cls.replace(/\s+/g, ' ').trim());
        changed = true;
    });

    // Make Contact Us button golden
    $('nav a:contains("Contact Us")').each(function() {
        let cls = $(this).attr('class') || '';
        cls = cls.replace(/bg-black|dark:bg-white|text-white|dark:text-black|hover:bg-amber-800|dark:hover:bg-amber-200/g, '');
        cls += ' bg-amber-500 text-black hover:bg-amber-400';
        $(this).attr('class', cls.replace(/\s+/g, ' ').trim());
        changed = true;
    });

    if (changed) {
        // Re-write without HTML/HEAD/BODY wrapper if it wasn't there? cheerio adds it if not careful.
        // Actually cheerio.load(content) maintains the original structure.
        fs.writeFileSync(filePath, $.html());
        console.log(`Updated ${file}`);
    }
});
console.log('Nav updates complete.');
