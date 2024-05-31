import '@testing-library/jest-dom';

import { afterEach, describe, expect, test } from 'vitest';
import { QuantityForm } from '~/components/Manifest/WasteLine/QuantityForm';
import { cleanup, renderWithProviders, screen } from '~/test-utils';

afterEach(() => cleanup());

describe('QuantityForm', () => {
  test('renders', () => {
    renderWithProviders(<QuantityForm />);
    expect(screen.getByText(/Container/i)).toBeInTheDocument();
  });
});
