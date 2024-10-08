import { createSelector } from '@reduxjs/toolkit';
import React, { useContext, useMemo } from 'react';
import { ButtonProps } from 'react-bootstrap';
import { FaFeather } from 'react-icons/fa';
import { ManifestContext } from '~/components/Manifest/ManifestForm';
import { Handler } from '~/components/Manifest/manifestSchema';
import { RcraApiUserBtn } from '~/components/Rcrainfo';
import { ProfileSlice, useGetProfileQuery } from '~/store';

interface QuickSignBtnProps extends ButtonProps {
  mtnHandler?: Handler;
  iconOnly?: boolean;
}

/**
 * Button for initiating a task to pull manifests from RCRAInfo for a given site
 * The button will be disabled if siteId (the EPA ID number) is not provided
 * @constructor
 */
export function QuickSignBtn({ mtnHandler, iconOnly = false, ...props }: QuickSignBtnProps) {
  const { nextSigningSite } = useContext(ManifestContext);

  const selectBySiteId = useMemo(() => {
    return createSelector(
      (res) => res.data,
      (_res, siteId) => siteId,
      (data: ProfileSlice, siteId) => {
        return data && data.sites ? data.sites[siteId] : undefined;
      }
    );
  }, []);

  const { userSite } = useGetProfileQuery(undefined, {
    selectFromResult: (res) => ({
      ...res,
      userSite: selectBySiteId(res, nextSigningSite?.epaSiteId),
    }),
  });
  if (!userSite) return <></>;

  if (mtnHandler && mtnHandler?.epaSiteId !== nextSigningSite?.epaSiteId) return <></>;

  if (nextSigningSite?.siteType === undefined) return <></>;

  return (
    <RcraApiUserBtn {...props}>
      {iconOnly ? '' : 'Sign '}
      <FaFeather />
    </RcraApiUserBtn>
  );
}
