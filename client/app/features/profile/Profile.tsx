import React, { ReactElement } from 'react';
import { Col, Container, Row } from 'react-bootstrap';
import { HtCard } from '~/components/legacyUi';
import { UserOrg } from '~/components/Org';
import { RcraProfile } from '~/components/RcraProfile';
import { Spinner } from '~/components/ui';
import { UserInfoForm } from '~/components/User';
import { useTitle } from '~/hooks';
import { useGetProfileQuery, useGetRcrainfoProfileQuery, useGetUserQuery } from '~/store';

/**
 * Display user profile, including their Haztrak information, their organization,
 * and their RCRAInfo profile.
 * @constructor
 */
export function Profile(): ReactElement {
  const { data: profile, isLoading: profileLoading } = useGetProfileQuery();
  const { data: user, isLoading: userLoading } = useGetUserQuery();
  const { data: rcrainfoProfile } = useGetRcrainfoProfileQuery('testuser1');
  const isLoading = profileLoading || userLoading;
  useTitle('Profile');

  if (isLoading || !user || !profile) {
    return <Spinner size="lg" />;
  }

  if (!profile || !user) {
    return <div>Error loading profile</div>;
  }

  return (
    <>
      <Container fluid className="py-2">
        <h1 className="tw-text-2xl tw-font-bold">Profile</h1>
        <Row className="my-3">
          <Col xs={12} lg={6} className="my-3">
            <HtCard title="User Information" className="h-100 my-2">
              <HtCard.Body>
                <UserInfoForm user={user} profile={profile} />
              </HtCard.Body>
            </HtCard>
          </Col>
          <Col xs={12} lg={6} className="my-3">
            <HtCard title="My Organization" className="h-100 my-2">
              <HtCard.Body>{profile && <UserOrg profile={profile} />}</HtCard.Body>
            </HtCard>
          </Col>
        </Row>
        <Row>
          <Col>
            <HtCard title="RCRAInfo Profile">
              <HtCard.Body>
                {rcrainfoProfile && <RcraProfile profile={rcrainfoProfile} />}
              </HtCard.Body>
            </HtCard>
          </Col>
        </Row>
      </Container>
    </>
  );
}