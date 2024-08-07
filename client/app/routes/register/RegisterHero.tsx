import logo from '/assets/img/haztrak-logos/high-resolution/png/haztrak-high-resolution-logo-black-on-transparent-background.png';
import { faFileLines, faPen, faSitemap } from '@fortawesome/free-solid-svg-icons';
import React from 'react';
import { Link } from 'react-router-dom';
import { FeatureDescription } from '~/components/UI';

export function RegisterHero() {
  return (
    <div className="tw-bg-light tw-container tw-mx-auto tw-min-h-screen tw-px-4 tw-py-5 tw-text-center">
      <img
        src={logo}
        alt="haztrak logo, hazardous waste tracking made easy."
        className="tw-my-3"
        style={{ width: 'auto', height: '100px' }}
      />
      <h1 className="tw-mb-0 tw-text-5xl tw-font-bold">Focus on Waste Management</h1>
      <h2 className="tw-pt-0 tw-text-4xl tw-font-semibold">Let us Handle the paperwork</h2>
      <div className="tw-mx-auto tw-max-w-lg">
        <p className="tw-my-2 tw-text-lg">
          The Resource Conservation and Recovery Act (RCRA) is complicated enough; don't make it
          more complicated with outdated hazardous waste management practices. Start electronically
          manifesting your waste shipments and take control of your data.
        </p>
        <div className="tw-flex tw-justify-center tw-gap-3">
          <button className="my-primary bg-gradient tw-rounded-lg tw-px-4 tw-py-2 tw-text-lg tw-text-white">
            Learn More
          </button>
          <Link to={'/login'}>
            <button className="tw-rounded-lg tw-border-4 tw-border-solid tw-border-green-600 tw-px-4 tw-py-2 tw-text-lg tw-text-green-700">
              Sign Up
            </button>
          </Link>
        </div>
      </div>
      <div className="tw-my-5 tw-grid tw-grid-cols-1 tw-gap-4 tw-pt-5 tw-text-left lg:tw-grid-cols-3">
        <div>
          <FeatureDescription title="Manifest" icon={faFileLines}>
            <p>
              Leverage the power of integration with EPA while creating, updating, or deleting
              electronic hazardous waste manifests to accurately capture the waste shipment.
            </p>
          </FeatureDescription>
        </div>
        <div>
          <FeatureDescription title="e-Sign" icon={faPen}>
            <p>
              Sign your electronic manifests to signify custody exchange without ever logging into
              EPA's e-Manifest system.
            </p>
          </FeatureDescription>
        </div>
        <div>
          <FeatureDescription title="Manage" icon={faSitemap}>
            <p>
              Organize sites to match company structure and give personnel the access and tools to
              get the job done with ease.
            </p>
          </FeatureDescription>
        </div>
      </div>
    </div>
  );
}
