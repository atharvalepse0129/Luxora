const fs = require('fs');
const path = require('path');

const dir = './';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const replacements = {
  'py-48': 'py-16',
  'py-32': 'py-16',
  'mb-64': 'mb-16',
  'mb-48': 'mb-16',
  'mb-32': 'mb-12',
  'mt-48': 'mt-16',
  'mt-32': 'mt-16',
  'pt-48': 'pt-24',
  'pt-32': 'pt-24',
  'gap-24': 'gap-12',
  'mb-24': 'mb-12'
};

files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf8');

  let updated = false;
  // Use regex to only match exact class names
  for (const [oldClass, newClass] of Object.entries(replacements)) {
    const regex = new RegExp(`\\b${oldClass}\\b`, 'g');
    if (regex.test(content)) {
      content = content.replace(regex, newClass);
      updated = true;
    }
  }

  if (updated) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Updated spacing in ${file}`);
  }
});
console.log('Finished updating spacing across all HTML files.');
