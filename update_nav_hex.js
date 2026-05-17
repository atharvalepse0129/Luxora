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

    // Update nav links to #D4AF37
    $('nav .hidden.md\\:flex.space-x-10 a, nav .hidden.md\\:flex.lg\\:space-x-14 a').each(function() {
        let cls = $(this).attr('class') || '';
        // Remove the amber classes we added previously
        cls = cls.replace(/text-amber-\d+|dark:text-amber-\d+|border-amber-\d+|dark:border-amber-\d+/g, '').replace(/\s+/g, ' ').trim();
        
        // Add specific hex gold color
        if (cls.includes('border-b')) {
            cls += ' text-[#D4AF37] border-[#D4AF37] hover:opacity-80';
        } else {
            cls += ' text-[#D4AF37] hover:opacity-80';
        }
        $(this).attr('class', cls.replace(/\s+/g, ' ').trim());
        $(this).removeAttr('style');
        changed = true;
    });

    // Revert Contact Us button to black
    $('nav a:contains("Contact Us")').each(function() {
        let cls = $(this).attr('class') || '';
        // Remove amber backgrounds and texts
        cls = cls.replace(/bg-amber-\d+|text-black|text-stone-900|hover:bg-amber-\d+/g, '').replace(/\s+/g, ' ').trim();
        // Add black classes
        cls += ' bg-black dark:bg-white text-white dark:text-black hover:opacity-80';
        $(this).attr('class', cls.replace(/\s+/g, ' ').trim());
        changed = true;
    });

    if (changed) {
        fs.writeFileSync(filePath, $.html());
        console.log(`Updated ${file}`);
    }
});
console.log('Nav updates with exact hex code complete.');
