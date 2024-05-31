import '@testing-library/jest-dom';
import { afterEach, describe, expect, test } from 'vitest';
import { cleanup, renderWithProviders, screen } from '~/test-utils';
import { ContactForm } from './ContactForm';

afterEach(() => {
  cleanup();
});

describe('ContactForm', () => {
  test('renders with basic information inputs', () => {
    renderWithProviders(<ContactForm handlerType={'generator'} />);
    expect(screen.getByText(/First Name/i)).toBeInTheDocument();
    expect(screen.getByText(/Last Name/i)).toBeInTheDocument();
  });
});
