import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        caseStudies: resolve(__dirname, 'case-studies.html'),
        blog: resolve(__dirname, 'blog.html'),
        contact: resolve(__dirname, 'contact.html'),
        designerBoutiques: resolve(__dirname, 'designer-boutiques.html'),
        premiumEthnicWear: resolve(__dirname, 'premium-ethnic-wear.html'),
        coutureWeddingWear: resolve(__dirname, 'couture-wedding-wear.html'),
        bespokeTailoring: resolve(__dirname, 'bespoke-tailoring.html'),
        luxuryFashionBrands: resolve(__dirname, 'luxury-fashion-brands.html'),
        privacyPolicy: resolve(__dirname, 'privacy-policy.html')
      }
    }
  }
})
