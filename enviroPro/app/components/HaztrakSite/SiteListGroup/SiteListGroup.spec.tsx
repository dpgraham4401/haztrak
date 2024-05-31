import '@testing-library/jest-dom';
import { screen } from '@testing-library/react';
import { afterEach, describe, expect, test } from 'vitest';
import { SiteListGroup } from '~/components/HaztrakSite/SiteListGroup/SiteListGroup';
import { cleanup, renderWithProviders } from '~/test-utils';
import { createMockHandler, createMockSite } from '~/test-utils/fixtures/mockHandler';

afterEach(() => {
  cleanup();
});

const mySite2Handler = createMockHandler({ epaSiteId: 'TXD0192837465' });

const mySite1 = createMockSite();
const mySite2 = createMockSite({ name: 'My Second Site', handler: mySite2Handler });

const mockSites = [mySite1, mySite2];

describe('SiteListGroup', () => {
  test('renders a list containing site names', () => {
    renderWithProviders(<SiteListGroup sites={mockSites} />);
    expect(screen.getByText(mySite1.name)).toBeInTheDocument();
    expect(screen.getByText(mySite2.name)).toBeInTheDocument();
  });
});
