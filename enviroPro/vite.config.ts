/// <reference types="vitest" />

import { vitePlugin as remix } from '@remix-run/dev';
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  server: {
    host: true,
    port: 3000,
  },
  plugins: [!process.env.VITEST && remix({ ssr: false }), tsconfigPaths()],
  test: {
    environment: 'jsdom',
    coverage: {
      provider: 'v8', // or 'istanbul'
      reporter: ['text', 'json', 'html'],
      exclude: [
        '**/node_modules/**',
        '**/build/**',
        '**/dist/**',
        '**/coverage/**',
        '**/public/**',
        '**/*.d.ts',
        '**/index.ts',
      ],
    },
    globals: true,
    setupFiles: ['setupTests.ts'],
  },
});
