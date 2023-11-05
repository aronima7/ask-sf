import { defineConfig, UserConfigExport } from 'vite'
import react from '@vitejs/plugin-react'

const build = process.env["BUILD"] === "true";
const config: UserConfigExport = {
  plugins: [react()]
}
if (!build) {
  config.server = {
    host: '127.0.0.1',
    port: 3000,
    open: 'http://localhost:3000/',
    // this is required to avoid CORS requests
    proxy: {
      '/api': 'http://localhost:8000/',
      '/user': 'http://localhost:8000/',
    }
  }
}
// https://vitejs.dev/config/
export default defineConfig(config);