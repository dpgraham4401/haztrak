import React, { forwardRef, ReactElement } from 'react';
import {
  Form,
  FormCheckProps,
  FormGroupProps,
  FormLabelProps,
  FormProps,
  FormSelectProps,
  InputGroup,
  InputGroupProps,
} from 'react-bootstrap';

export function HtForm(props: FormProps): ReactElement {
  return <Form {...props}>{props.children}</Form>;
}

// eslint-disable-next-line react/display-name
HtForm.Group = (props: FormGroupProps): ReactElement => (
  <Form.Group {...props} className="mb-2">
    {props.children}
  </Form.Group>
);

// eslint-disable-next-line react/display-name
HtForm.InputGroup = (props: InputGroupProps): ReactElement => (
  <InputGroup {...props} className="mb-2">
    {props.children}
  </InputGroup>
);

// eslint-disable-next-line react/display-name
HtForm.Label = (props: FormLabelProps): ReactElement => (
  <Form.Label {...props} className={`mb-0 fw-bold ${props.className}`}>
    {props.children}
  </Form.Label>
);

// eslint-disable-next-line react/display-name
HtForm.Check = forwardRef<HTMLInputElement, FormCheckProps>(
  (props: FormCheckProps, ref: React.Ref<HTMLInputElement>) => {
    return (
      <Form.Check ref={ref} {...props}>
        {props.children}
      </Form.Check>
    );
  }
);

// eslint-disable-next-line react/display-name
HtForm.Select = forwardRef<HTMLSelectElement, FormSelectProps>(
  (props: FormSelectProps, ref: React.Ref<HTMLSelectElement>) => {
    return (
      <Form.Select ref={ref} {...props}>
        {props.children}
      </Form.Select>
    );
  }
);

// eslint-disable-next-line react/display-name
HtForm.Switch = forwardRef<HTMLInputElement, FormCheckProps>(
  (props: FormCheckProps, ref: React.Ref<HTMLInputElement>) => {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const { children, dangerouslySetInnerHTML, ...rest } = props;
    return (
      <Form.Check ref={ref} {...rest} type="switch">
        {children}
      </Form.Check>
    );
  }
);
