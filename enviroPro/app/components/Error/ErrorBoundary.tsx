import { Component, ReactNode } from 'react';
import { Alert, Button, Col, Container, Row } from 'react-bootstrap';

interface Props {
  children?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: undefined,
  };

  public static getDerivedStateFromError(error: Error): State {
    // Update state so the next render will show the fallback UI.
    return { hasError: true, error: error };
  }

  // Todo: do something with error info (e.g., send to new endpoint and log)
  public componentDidCatch(error: Error) {
    console.error('Haztrak error:', error);
  }

  public render() {
    if (this.state.hasError) {
      return (
        <Container className="p-4 d-flex justify-content-center">
          <Col className="col-lg-8 col-md-10">
            <Row className="d-flex justify-content-center">
              <i className="text-danger h1 fas fa-bug"></i>
            </Row>
            <Row className="d-flex justify-content-center">
              <h4 className="d-flex justify-content-center">Something`&apos;`s Broken</h4>
            </Row>
            <Row className="d-flex justify-content-center">
              Don`&apos;`t worry, we`&apos;`re working on it!
            </Row>
            <Row className="d-flex justify-content-center pt-4">
              <Alert key="danger" variant="danger">
                {`${this.state.error}`}
              </Alert>
            </Row>
            <div className="mx-1 d-flex flex-row-reverse">
              <Button variant="danger" onClick={() => this.setState({ hasError: false })}>
                Go back
              </Button>
            </div>
          </Col>
        </Container>
      );
    }

    return this.props.children;
  }
}
