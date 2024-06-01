import { ReactElement } from 'react';
import { Container } from 'react-bootstrap';
import { LoginForm } from '~/components/Auth';
import { useTitle } from '~/hooks';
import logo from './assets/haztrak-low-resolution-logo-black-on-transparent-background.svg';

/**
 * Haztrak Login component, redirects if user is already logged in
 * @constructor
 */
export default function Login(): ReactElement {
  useTitle('Login');

  return (
    <Container fluid className="bg-light vh-100 align-items-center py-5 d-flex">
      <div className="m-auto" style={{ maxWidth: 330 }}>
        <img
          src={logo}
          alt="haztrak logo, hazardous waste tracking made easy."
          width="auto"
          height={100}
          className="my-3"
        />
        <h1 className="h3 mb-3 text-start">Please Sign In</h1>
        <LoginForm />
      </div>
    </Container>
  );
}
