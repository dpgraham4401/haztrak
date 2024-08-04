import { cleanup, renderWithProviders, screen } from 'app/mocks';
import { createMockHandler } from '~/mocks/fixtures';
import { afterEach, describe, expect, test } from 'vitest';
import { TsdfSection } from './TsdfSection';

afterEach(() => cleanup());

const TestComponent = () => {
  return <TsdfSection setupSign={() => undefined} signAble={true} />;
};

describe('TsdfSection', () => {
  test('renders', () => {
    renderWithProviders(<TestComponent />, {
      useFormProps: {
        values: {
          status: 'NotAssigned',
          designatedFacility: createMockHandler({ epaSiteId: 'VATEST123' }),
        },
      },
    });
    expect(screen.getByText(/vatest123/i)).toBeInTheDocument();
  });
});
