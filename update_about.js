const fs = require('fs');

let content = fs.readFileSync('about.html', 'utf8');

// Title & Meta
content = content.replace(
    '<title>About LUXORA | The Art of Modern Elegance</title>',
    '<title>Luxury Brand Digital Marketing Agency | Luxora</title>\n<meta name="description" content="Luxora is a luxury digital marketing agency focused on high-end brand positioning, aspirational storytelling, and precision-driven digital experiences.">'
);

// Hero Subheading
content = content.replace(
    'Redefining the digital landscape through architectural precision and a relentless pursuit of prestige.',
    'Luxora is a luxury brand digital marketing firm, which exists as a brand house and solely with the brands that operate in the top tier of human desire. We are not fashionable - we make fashions. Our product will change an emerging brand in the realm of fashion, hospitality, and lifestyle to garner attention, gather cultural impact, and turn desire into holding a long-term loyalty. We have been helping premium brands to do so since 2018.'
);

// Quote
content = content.replace(
    /"Luxury is not about selling more. It’s about being <span class="font-bold not-italic">desired more.<\/span>"/,
    '"Luxury is not about making more sales. It lies upon the desirability."'
);

// Methodology Title
content = content.replace(
    '<h2 class="text-5xl font-serif">The Architectural Approach</h2>',
    '<h2 class="text-5xl font-serif">The Globalization of High-End Brand Marketing through architecture</h2>'
);

// 01 Beauty
content = content.replace(
    '<h3 class="text-2xl font-serif font-bold mb-6">Attract</h3>',
    '<h3 class="text-2xl font-serif font-bold mb-6">Beauty</h3>'
);
content = content.replace(
    'We curate visual experiences that command immediate attention, leveraging high-contrast aesthetics and intentional whitespace to create an aura of exclusivity.',
    'We create catchy images. Conscious blank space, high contrast aesthetic appearance, selective images create an effect of exclusivity, which stops your ideal audience and makes you stare. Luxury brand digital marketing plans are intended in brands that will not be ignored.'
);

// 02 Position
content = content.replace(
    'Strategic narrative framing that elevates your brand from a service provider to a cultural authority, ensuring you occupy the highest tier of market desire.',
    'We make your brand something more than a service provider, a cultural authority. Decent narrative framing and premium brand storytelling will have your brand in the carve like nothing else in the market - it spliches the luxury market of the high net worths that value luxury and prestige over cost.'
);

// 03 Transform
content = content.replace(
    '<h3 class="text-2xl font-serif font-bold mb-6">Convert</h3>',
    '<h3 class="text-2xl font-serif font-bold mb-6">Transform</h3>'
);
content = content.replace(
    'Precision-engineered interfaces designed for a seamless, frictionless journey that transforms aspiration into definitive brand loyalty.',
    'We design online experiences that are flawless and translating desire into eventual brand loyalty. Every strategy under our upscale brand promotion strategy has been crafted to make the choice to choose you impossible since the opening pages and the rest of the digital landscape.'
);

// Founder's Letter
content = content.replace(
    /<div class="space-y-8 font-body text-lg text-on-surface-variant leading-relaxed">[\s\S]*?<\/div>/,
    `<div class="space-y-8 font-body text-lg text-on-surface-variant leading-relaxed">\n<p>\n                            The luxury in the digital noise era is silence.\n                        </p>\n<p>\n                            We think the art of art is the not to be carried out on the gratuitous at Luxora. We are under volume based who are luxury digital marketing agency but value based, perception based and legacy based.\n                        </p>\n<p>\n                            It is not everything about aesthetic what we do. It is in terms of creating smart brand names that will not be affected by the trends. Each pixel, each line of text, each digital surface is more like an architectural element - designed to be built to withstand decades not seasons.\n                        </p>\n<p>\n                            Brands are only one of the things we build. We design luxurious online experiences to people who know that the worth of a thing is judged in the levels of yearning and not messages of an advertisement. Luxora wants to partner with your brand in case it is not going to be just found, in other words, desired.\n                        </p>\n</div>`
);

// CTA
content = content.replace(
    '<h2 class="text-5xl font-serif mb-12">Elevate Your Presence</h2>',
    '<h2 class="text-5xl font-serif mb-6">Improve Your Brand Image</h2>\n<p class="font-body text-on-surface-variant mb-12 max-w-2xl mx-auto">Your brand cannot be promoted using the typical playbook of the digital marketing industry. It possesses a partner that is worth looking at and positioning it in the very top of its market through the correct knowledge, vision, and cultural fluency.</p>'
);
content = content.replace(
    'Inquire for Collaboration',
    'Request Co-operation'
);

// Footer Copyright
content = content.replace(
    '© 2024 LUXORA. ALL RIGHTS RESERVED.',
    '© 2025 LUXORA. All Rights Reserved.'
);

fs.writeFileSync('about.html', content);
console.log('Update complete.');
