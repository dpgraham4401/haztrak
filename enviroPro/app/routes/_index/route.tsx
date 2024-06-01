import type { MetaFunction } from '@remix-run/node';
import { ReactElement } from 'react';
import { Accordion, Button, Col, Container, Row } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import {
  GeneratorStatusAreaChart,
  ManifestCountBarChart,
  ManifestStatusPieChart,
} from '~/components/Charts';
import { NewManifestBtn } from '~/components/Manifest';
import { HtButton, HtCard } from '~/components/UI';
import { addAlert, useAppDispatch } from '~/store';

export const meta: MetaFunction = () => {
  return [
    { title: 'Haztrak | DashBoard' },
    { name: 'description', content: 'Your home for tracking your waste' },
  ];
};

/** Dashboard page for logged-in user*/
export default function Dashboard(): ReactElement {
  const dispatch = useAppDispatch();

  return (
    <Container className="py-2 pt-3">
      <Row className="my-3">
        <Accordion className="px-0">
          <Accordion.Item eventKey={'0'}>
            <Accordion.Header title="Getting Started">
              Welcome, let&apo;s get started
            </Accordion.Header>
            <Accordion.Body>
              <Row>
                <h3>Features</h3>
                <hr />
                <Col className="text-center">
                  <NewManifestBtn />
                  <p>
                    Create your first electronic manifest to track hazardous waste without ever
                    logging into EPA&apos;s RCRAInfo system
                  </p>
                </Col>
                <Col className="text-center">
                  <Link to={'/profile'}>
                    <Button variant="info text-light">Profile</Button>
                  </Link>
                  <p>
                    Update your Profile with your RCRAInfo API ID & key so you can electronically
                    manifest your waste through e-Manifest.
                  </p>
                </Col>
                <Col className="text-center">
                  <Link to={'/site'}>
                    <Button variant="dark">My Sites</Button>
                  </Link>
                  <p>
                    View your site&apos;s information, check that EPA has the right information.
                  </p>
                </Col>
              </Row>
              <h3>Alerts</h3>
              <hr />
              <Row className="align-content-start">
                <Col className="text-center">
                  <HtButton
                    variant="danger"
                    onClick={() => {
                      dispatch(
                        addAlert({
                          message: 'Oh No!',
                          autoClose: 1000,
                          type: 'warning',
                        })
                      );
                    }}
                  >
                    Show Warning
                  </HtButton>
                  <p>Check out what an alert will look like</p>
                </Col>
              </Row>
            </Accordion.Body>
          </Accordion.Item>
        </Accordion>
      </Row>
      <Row xs={1} lg={2}>
        <Col className="my-3">
          <HtCard title="Calculated Status" className="p-2">
            <GeneratorStatusAreaChart />
          </HtCard>
        </Col>
        <Col className="my-3">
          <HtCard title="Manifest by Status" className="p-2">
            <ManifestStatusPieChart />
          </HtCard>
        </Col>
      </Row>
      <Row>
        <Col>
          <HtCard title="Manifest count" className="p-2">
            <ManifestCountBarChart />
          </HtCard>
        </Col>
      </Row>
    </Container>
  );
}
