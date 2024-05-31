import { screen } from '@testing-library/react';
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { describe, expect, test } from 'vitest';
import { SiteSelect } from '~/components/Manifest/SiteSelect/SiteSelect';
import { renderWithProviders } from '~/test-utils';

function TestComponent() {
  const [selected, setSelected] = useState();
  const { control } = useForm();
  // @ts-ignore
  return <SiteSelect value={selected} handleChange={setSelected} control={control} />;
}

describe('SiteSelect', () => {
  test('renders', () => {
    renderWithProviders(<TestComponent />);
    expect(screen.queryByTestId('siteSelect')).toBeDefined();
  });
});
