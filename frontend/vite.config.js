// Inicio vite.config.js

// frontend/vite.config.js

// Archivo de configuración de Vite para el proyecto frontend

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      workbox: {
        // Estrategias de cache más agresivas para actualización
        cleanupOutdatedCaches: true,
        clientsClaim: true,
        skipWaiting: true,
      },
      manifest: {
        name: 'CalorSOS - Alertas de Calor',
        short_name: 'CalorSOS',
        description: 'App para alertas de calor y puntos de hidratación',
        start_url: '/',
        display: 'standalone',
        background_color: '#ffffff',
        theme_color: '#007bff',
        icons: [
          {
            src: '/logo-192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/logo-512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      },
      // Importante: agrega versionado a los assets
      devOptions: {
        enabled: false
      }
    })
  ],
  build: {
    // Agrega hash a los archivos para evitar cache
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].[hash].js`,
        chunkFileNames: `assets/[name].[hash].js`,
        assetFileNames: `assets/[name].[hash].[ext]`
      }
    }
  }
})

// Fin vite.config.js