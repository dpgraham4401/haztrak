import { describe, expect, test } from 'vitest';
import { addError, setupStore } from '~/store';

describe('Error Slice', () => {
  test('initial state is empty', async () => {
    const store = setupStore();
    const state = store.getState();
    expect(state.error.errors).toEqual([]);
  });
  test('adding error appends to state', async () => {
    const store = setupStore();
    store.dispatch(addError({ id: 'foo', message: 'bar', status: 404 }));
    const state = store.getState();
    expect(state.error.errors.length).toEqual(1);
  });
  test('selecting all returns full list of errors', async () => {
    const store = setupStore();
    const errors = [
      { id: 'foo', message: 'bar', status: 404 },
      { id: '1', message: '1', status: 404 },
    ];
    errors.forEach((error) => store.dispatch(addError(error)));
    const state = store.getState();
    expect(state.error.errors.length).toEqual(errors.length);
  });
});
