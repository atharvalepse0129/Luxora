const fs = require('fs');

const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));

for (const file of files) {
  let content = fs.readFileSync(file, 'utf-8');
  
  // Replace nav logo
  content = content.replace(
      /class="h-24 md:h-28 w-auto object-contain"/g, 
      'class="h-24 md:h-28 w-auto object-contain scale-[2] md:scale-[2.5] origin-left dark:invert"'
  );
  
  // Replace bespoke tailoring specific logo format if any
  content = content.replace(
      /<a href="\/" class="flex-shrink-0 flex items-center transition-opacity hover:opacity-80 duration-500"><img src="\/logo.png" alt="Luxora" class="h-24 md:h-28 w-auto object-contain"><\/a>/g,
      '<a href="/" class="flex-shrink-0 flex items-center transition-opacity hover:opacity-80 duration-500"><img src="/logo.png" alt="Luxora" class="h-24 md:h-28 w-auto object-contain scale-[2] md:scale-[2.5] origin-left dark:invert"></a>'
  );

  // Replace standard footer logos
  content = content.replace(
      /class="h-20 w-auto object-contain"/g, 
      'class="h-20 w-auto object-contain scale-[2] md:scale-[2.5] origin-left dark:invert"'
  );

  // Replace blog specific footer logo
  content = content.replace(
      /class="w-auto object-contain grayscale opacity-70 hover:grayscale-0 hover:opacity-100 transition-all duration-500 h-20"/g,
      'class="w-auto object-contain grayscale opacity-70 hover:grayscale-0 hover:opacity-100 transition-all duration-500 h-20 scale-[2] md:scale-[2.5] origin-left dark:invert"'
  );

  fs.writeFileSync(file, content);
}

console.log("Logo visibility classes applied to all HTML files.");
