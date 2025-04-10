import { RenderHookResult, RenderOptions, render, renderHook } from '@testing-library/react';
import React, { PropsWithChildren, ReactElement } from 'react';
import { FormProvider, UseFormProps, useForm } from 'react-hook-form';
import { Provider } from 'react-redux';
import { MemoryRouter, MemoryRouterProps } from 'react-router';
import { AppStore, RootState, setupStore } from '~/store';

interface ExtendedRenderOptions extends Omit<RenderOptions, 'queries'> {
  preloadedState?: Partial<RootState>;
  store?: AppStore;
  useFormProps?: UseFormProps;
  routerProps?: MemoryRouterProps;
}

/**
 *
 * @description
 * utility wrapper for @testing-library/react, so we do not need to
 * use Redux store Provider and BrowserRouter in all tests, see
 * https://testing-library.com/docs/react-testing-library/setup/#custom-render
 *
 * for components expected to be rendered within FormProvider context,
 * see https://github.com/react-hook-form/react-hook-form/discussions/3815
 * @example
 *describe('HelloWorld Test Suite', () => {
 *  test('test name', () => {
 *    renderWithProviders(<HelloWorldComponent />);
 *    expect(screen.getByText(/Hello World/i)).toBeInTheDocument();
 *  });
 *});
 */
export function renderWithProviders(
  ui: React.ReactElement,
  {
    preloadedState = {}, // an object with partial slices of our redux state
    store = setupStore(preloadedState), // Automatically create a store instance if no store was passed in
    useFormProps = {}, // react-hook-form useForm function options
    routerProps,
    ...renderOptions // react-testing library function options
  }: ExtendedRenderOptions = {} // default to empty object
) {
  function Wrapper({ children }: PropsWithChildren<NonNullable<unknown>>): ReactElement {
    const formMethods = useForm(useFormProps);
    return (
      <Provider store={store}>
        <MemoryRouter {...routerProps}>
          <FormProvider {...formMethods}>{children}</FormProvider>
        </MemoryRouter>
      </Provider>
    );
  }

  return { store, ...render(ui, { wrapper: Wrapper, ...renderOptions }) };
}

export function renderHookWithProviders<T>(
  hook: () => T,
  {
    preloadedState = {},
    store = setupStore(preloadedState),
    useFormProps = {},
  }: ExtendedRenderOptions = {}
): RenderHookResult<T, unknown> {
  function Wrapper({ children }: PropsWithChildren<NonNullable<unknown>>): ReactElement {
    const formMethods = useForm(useFormProps);
    return (
      <Provider store={store}>
        <MemoryRouter>
          <FormProvider {...formMethods}>{children}</FormProvider>
        </MemoryRouter>
      </Provider>
    );
  }

  return { ...renderHook(hook, { wrapper: Wrapper }) };
}
