import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';

import { afterAll, beforeAll, describe, expect, test } from 'vitest';
import { renderWithProviders, screen } from '~/mocks';
import { createMockHandler, createMockSite } from '~/mocks/fixtures/mockHandler';
import { mockSiteEndpoints, mockUserEndpoints } from '~/mocks/handlers';
import { SiteList } from './SiteList';

const mockHandler1 = createMockHandler({ epaSiteId: 'VAT987654321' });
const mockHandler2 = createMockHandler({ epaSiteId: 'VAT123456789' });
const mockSites = [
  createMockSite({ handler: mockHandler1 }),
  createMockSite({ handler: mockHandler2 }),
];
const server = setupServer(...mockUserEndpoints, ...mockSiteEndpoints);

beforeAll(() => server.listen());
afterAll(() => server.close());

describe('SiteList component', () => {
  test('renders', () => {
    renderWithProviders(<SiteList />, {});
  });
  test('displays all sites a user has access to', async () => {
    server.use(
      http.get(`${process.env.NEXT_PUBLIC_HT_API_URL}/api/site`, () => {
        return HttpResponse.json(mockSites, { status: 200 });
      })
    );
    renderWithProviders(<SiteList />);
    const numIds = await screen.findAllByRole('listitem');
    expect(numIds.length).toEqual(mockSites.length);
  });
});
