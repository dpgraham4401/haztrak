import { RemixBrowser } from '@remix-run/react';
import { startTransition, StrictMode } from 'react';
import { hydrateRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { rootStore } from '~/store';

startTransition(() => {
  hydrateRoot(
    document,
    <StrictMode>
      <Provider store={rootStore}>
        <RemixBrowser />
      </Provider>
    </StrictMode>
  );
});
