import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import { analyzer } from 'vite-bundle-analyzer'

// https://vite.dev/config/
export default defineConfig(() => {
  return ({
    plugins: [
      react(),
      analyzer({
        enabled: false,
      })
    ],
    build: {
      rollupOptions: {
        output: {
          dir: "../dist"
        }
      }
    },
    server: {
      proxy: {
        '/api': {
          target: 'http://localhost:8000',
        }
      }
    }
  });
})
