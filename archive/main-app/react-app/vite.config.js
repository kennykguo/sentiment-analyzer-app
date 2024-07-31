import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [react()],
//   root: 'react-app',
//   build: {
//     outDir: '../backend/static'
//   }
// })

export default defineConfig({
    plugins: [react()],
    build: {
      outDir: '../backend/static'
    },
    server: {
      open: true, // Opens the browser on server start
      port: 5127 // Set the desired port
    }
  });