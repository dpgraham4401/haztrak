import '@testing-library/jest-dom';
import { afterEach, describe, expect, test } from 'vitest';
import { PhoneForm } from '~/components/Manifest/Contact';
import { cleanup, renderWithProviders, screen } from '~/test-utils';

afterEach(() => {
  cleanup();
});

describe('PhoneForm', () => {
  test('renders', () => {
    renderWithProviders(<PhoneForm handlerType={'generator'} />);
    expect(screen.getByText(/Phone Number/i)).toBeInTheDocument();
    expect(screen.getByText(/Extension/i)).toBeInTheDocument();
  });
});
