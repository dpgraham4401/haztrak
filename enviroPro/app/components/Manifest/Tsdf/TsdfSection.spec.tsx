import '@testing-library/jest-dom';
import { afterEach, describe, expect, test } from 'vitest';
import { cleanup, renderWithProviders, screen } from '~/test-utils';
import { createMockHandler } from '~/test-utils/fixtures';
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
