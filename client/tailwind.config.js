import colors from 'tailwindcss/colors';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./app/**/*.{js,ts,jsx,tsx}'],
  theme: {
    theme: {
      colors: {
        primary: colors.sky,
      },
    },
    extend: {},
  },
  prefix: 'tw-',
  corePlugins: { preflight: false },
  plugins: [],
};
