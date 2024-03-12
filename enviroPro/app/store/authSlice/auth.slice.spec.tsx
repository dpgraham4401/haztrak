import '@testing-library/jest-dom';
import { afterEach, describe, expect, test, vi } from 'vitest';
import { removeCredentials, selectAuthenticated, setCredentials, setupStore } from '~/store';

const getItemSpy = vi.spyOn(Storage.prototype, 'getItem');
const setItemSpy = vi.spyOn(Storage.prototype, 'setItem');
const removeItemSpy = vi.spyOn(Storage.prototype, 'removeItem');

describe('auth slice', () => {
  afterEach(() => {
    getItemSpy.mockClear();
    setItemSpy.mockClear();
    removeItemSpy.mockClear();
  });
  test('our localStorage mocks are working', () => {
    const value = 'test';
    localStorage.setItem('token', value);
    expect(setItemSpy).toHaveBeenCalled();
    const foo = localStorage.getItem('token');
    expect(setItemSpy).toHaveBeenCalled();
    expect(foo).toBe(value);
  });
  test('initial state is unauthenticated', async () => {
    const store = setupStore();
    const state = store.getState();
    const isAuthenticated = selectAuthenticated(state);
    expect(isAuthenticated).toBeFalsy();
  });
  test('returns true when authenticated', async () => {
    const store = setupStore({ auth: { token: 'foo' } });
    const state = store.getState();
    const isAuthenticated = selectAuthenticated(state);
    expect(isAuthenticated).toBeTruthy();
  });
  test('setCredentials stores the token in local storage', async () => {
    const store = setupStore();
    store.dispatch(setCredentials({ token: 'mockToken' }));
    expect(setItemSpy).toHaveBeenCalled();
  });
  test('tokens are removed from localStorage on logout', async () => {
    const store = setupStore();
    localStorage.setItem('token', 'mockToken');
    store.dispatch(removeCredentials());
    expect(removeItemSpy).toHaveBeenCalled();
  });
});
