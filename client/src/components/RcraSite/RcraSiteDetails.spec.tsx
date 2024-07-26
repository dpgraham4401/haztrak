import '@testing-library/jest-dom';
import { RcraSiteDetails } from 'src/components/RcraSite';
import React from 'react';
import { cleanup, renderWithProviders, screen } from 'src/test-utils';
import { createMockMTNHandler } from 'src/test-utils/fixtures';
import { afterEach, describe, expect, test } from 'vitest';

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
