import '@testing-library/jest-dom';
import { cleanup, fireEvent, render, screen } from '@testing-library/react';

import { afterEach, describe, expect, test } from 'vitest';
import { HtTooltip } from '~/components/UI';

afterEach(() => {
  cleanup();
});

describe('HtTooltip', () => {
  test('renders', async () => {
    render(
      <HtTooltip text={'Chicken butt!'}>
        <p>Guess what?</p>
      </HtTooltip>
    );
    expect(screen.getByText('Guess what?')).toBeInTheDocument();
    fireEvent.mouseOver(screen.getByText('Guess what?'));
    expect(await screen.findByText('Chicken butt!')).toBeInTheDocument();
  });
});
