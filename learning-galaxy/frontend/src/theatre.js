// src/theatre.js
import { getProject } from '@theatre/core';

// Conditionally initialize the studio editor only in development mode
if (import.meta.env.DEV) {
  import('@theatre/studio').then((studio) => {
    studio.default.initialize();
  });
}

// Create and export the main animation "sheet"
export const demoSheet = getProject('Learning Galaxy').sheet('Main Scene');