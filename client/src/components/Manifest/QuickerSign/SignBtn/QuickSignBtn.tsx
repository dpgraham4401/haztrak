import { faFeather } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { ManifestContext } from 'components/Manifest/ManifestForm';
import { Handler, RcraSiteType } from 'components/Manifest/manifestSchema';
import { RcraApiUserBtn } from 'components/Rcrainfo';
import React, { useContext } from 'react';
import { ButtonProps } from 'react-bootstrap';
import { siteByEpaIdSelector, useAppSelector } from 'store';

interface QuickerSignData {
  handler: Handler | undefined;
  siteType: RcraSiteType;
}

interface QuickSignBtnProps extends ButtonProps {
  siteType?: RcraSiteType;
  mtnHandler?: Handler;
  handleClick: (data: QuickerSignData) => void;
  iconOnly?: boolean;
}

/**
 * Button for initiating a task to pull manifests from RCRAInfo for a given site
 * The button will be disabled if siteId (the EPA ID number) is not provided
 * @constructor
 */
export function QuickSignBtn({
  siteType,
  mtnHandler,
  handleClick,
  iconOnly = false,
  ...props
}: QuickSignBtnProps) {
  const { nextSigningSite } = useContext(ManifestContext);
  // if next site to sign is not one of the user's sites, don't show the button
  if (!useAppSelector(siteByEpaIdSelector(nextSigningSite?.epaSiteId))) return <></>;

  if (mtnHandler && mtnHandler?.epaSiteId !== nextSigningSite?.epaSiteId) return <></>;

  if (nextSigningSite?.siteType === undefined) return <></>;

  return (
    <RcraApiUserBtn
      onClick={() => {
        // @ts-ignore
        handleClick({ handler: mtnHandler, siteType: nextSigningSite?.siteType.toLowerCase() });
      }}
      {...props}
    >
      {iconOnly ? '' : 'Sign '}
      <FontAwesomeIcon icon={faFeather} />
    </RcraApiUserBtn>
  );
}
