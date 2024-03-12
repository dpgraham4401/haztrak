import { describe, expect, test } from 'vitest';
import { renderWithProviders } from '~/test-utils';
import { Org } from './Org';

describe('Test Setup', () => {
  test('runs tests', () => {
    renderWithProviders(<Org />);
    expect(true).toBeTruthy();
  });
});
