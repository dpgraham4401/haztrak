import '@testing-library/jest-dom';

import { afterEach, describe, expect, test } from 'vitest';
import { RcraSiteDetails } from '~/components/RcraSite';
import { cleanup, renderWithProviders, screen } from '~/test-utils';
import { createMockMTNHandler } from '~/test-utils/fixtures';

afterEach(() => {
  cleanup();
});

describe('RcraSiteDetails', () => {
  test('displays the handlers information', () => {
    const handler = createMockMTNHandler();
    renderWithProviders(<RcraSiteDetails handler={handler} />);
    expect(screen.getByText(handler.name)).toBeInTheDocument();
    expect(screen.getByText(handler.epaSiteId)).toBeInTheDocument();
  });
  test('does not display undefined when part of address is missing', () => {
    const minimumAddressHandler = createMockMTNHandler({
      siteAddress: {
        address1: '123 main st.',
        state: { code: 'Tx' },
      },
    });
    renderWithProviders(<RcraSiteDetails handler={minimumAddressHandler} />);
    expect(screen.queryByText(/undefined/)).not.toBeInTheDocument();
  });
});