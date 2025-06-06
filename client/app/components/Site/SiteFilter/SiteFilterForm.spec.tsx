import { screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import React, { useState } from 'react';
import { useSearchParams } from 'react-router';
import { afterEach, describe, expect, test } from 'vitest';
import { SiteFilterForm } from '~/components/Site/SiteFilter/SiteFilterForm';
import { cleanup, renderWithProviders } from '~/mocks';
import { createMockHandler, createMockSite } from '~/mocks/fixtures/mockHandler';

afterEach(() => {
  cleanup();
});

const mySite2Handler = createMockHandler({ epaSiteId: 'TXD0192837465' });

const mySite1 = createMockSite();
const mySite2 = createMockSite({ name: 'My Second Site', handler: mySite2Handler });

const mockSites = [mySite1, mySite2];

const TestComponent = () => {
  const [filteredSites, setFilteredSites] = useState(mockSites);
  const [searchParams] = useSearchParams();
  const siteFilter = searchParams.get('q') ?? undefined;
  return (
    <div>
      <SiteFilterForm sites={filteredSites} setFilteredSites={setFilteredSites} />
      <p>url parameter: {siteFilter}</p>
    </div>
  );
};

describe('SiteFilterForm', () => {
  test('renders ', () => {
    renderWithProviders(<TestComponent />);
    expect(screen.getByRole('form')).toBeInTheDocument();
  });
  test('URL query parameter is empty by default', () => {
    renderWithProviders(<TestComponent />);
    expect(screen.getByText(/url parameter:$/i)).toBeInTheDocument();
  });
  test('sets URL query parameter on submit', async () => {
    const userInput = 'TXD';
    const user = userEvent.setup();
    renderWithProviders(<TestComponent />);
    const filterField = screen.getByRole('searchbox');
    await user.click(filterField);
    await user.type(filterField, userInput);
    await user.type(filterField, '{enter}');
    expect(screen.getByText(new RegExp(`url parameter: ${userInput}`, 'i'))).toBeInTheDocument();
  });
});
