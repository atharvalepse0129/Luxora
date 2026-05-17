const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));

const linksMap = {
  'Home': '/',
  'About': '/about.html',
  'Services': '/services.html',
  'Case Studies': '/case-studies.html',
  'Blog': '/blog.html',
  'Contact': '/contact.html',
  'Contact Us': '/contact.html',
  'Apply for Partnership': '/contact.html',
  'Get in Touch': '/contact.html',
  'Request a Private Strategy Call': '/contact.html',
  'Elevate Your Brand': '/contact.html',
  'Apply for a Private Strategy Session': '/contact.html',
  'Apply for a Strategy Session': '/contact.html',
  'Book Consultation': '/contact.html',
};

const sectorMap = {
  'Luxury Fashion Brands: Men & Women': '/luxury-fashion-brands.html',
  'Designer Boutiques': '/designer-boutiques.html',
  'Bespoke Tailoring Brands': '/bespoke-tailoring.html',
  'Couture and Wedding Wear Designers': '/couture-wedding-wear.html',
  'Premium Ethnic Wear Brands': '/premium-ethnic-wear.html',
  'Luxury Fashion Brands': '/luxury-fashion-brands.html',
  'Couture & Wedding Wear': '/couture-wedding-wear.html',
  'Bespoke Tailoring': '/bespoke-tailoring.html',
  'Premium Ethnic Wear': '/premium-ethnic-wear.html'
};

for (const file of files) {
  const content = fs.readFileSync(file, 'utf-8');
  const $ = cheerio.load(content);
  
  // Find all anchor tags
  $('a').each(function() {
    const text = $(this).text().trim().replace(/\s+/g, ' ');
    
    // Exact mapping matches
    if (linksMap[text]) {
      $(this).attr('href', linksMap[text]);
    } 
    // Sector links - if the anchor is part of a card
    else if (text === 'Explore Sector' || text === 'View Case Study' || text === 'Explore Service' || text === 'Explore Strategy' || text === 'Explore Services') {
      const parentTitle = $(this).parent().find('h4, h3, h2, h5').text().trim().replace(/\s+/g, ' ');
      if (parentTitle && sectorMap[parentTitle]) {
        $(this).attr('href', sectorMap[parentTitle]);
      }
    }
  });

  // Buttons that should act as links
  $('button').each(function() {
    const text = $(this).text().trim().replace(/\s+/g, ' ');
    if (linksMap[text]) {
      // Modify button to be an anchor with identical classes but semantic a tag
      const href = linksMap[text];
      const cls = $(this).attr('class');
      const replacement = `<a href="${href}" class="${cls}">${$(this).html()}</a>`;
      $(this).replaceWith(replacement);
    } else if (/strategy/i.test(text) || /contact/i.test(text) || /partnership/i.test(text)) {
      const href = '/contact.html';
      const cls = $(this).attr('class');
      const replacement = `<a href="${href}" class="${cls}">${$(this).html()}</a>`;
      $(this).replaceWith(replacement);
    }
  });

  // Update navbar "LUXORA" logo to point to home
  $('div:contains("LUXORA")').each(function() {
      if ($(this).hasClass('font-serif') && $(this).hasClass('tracking-[0.2em]')) {
          const cls = $(this).attr('class');
          $(this).replaceWith(`<a href="/" class="${cls}">LUXORA</a>`);
      }
  });

  fs.writeFileSync(file, $.html());
}

console.log('Successfully connected all pages.');
