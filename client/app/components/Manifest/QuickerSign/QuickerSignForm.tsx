import React, { useEffect, useState } from 'react';
import { Button, Col, Container, Form, ListGroup, Row, Stack } from 'react-bootstrap';
import { SubmitHandler, useForm } from 'react-hook-form';
import { FaFileSignature, FaPen } from 'react-icons/fa';
import { useNavigate } from 'react-router';
import { z } from 'zod';
import { Transporter } from '~/components/Manifest/Transporter';
import { Handler, RcraSiteType } from '~/components/Manifest/manifestSchema';
import { HtForm } from '~/components/legacyUi';
import { useProgressTracker } from '~/hooks';
import { addTask, updateTask, useAppDispatch, useSignEManifestMutation } from '~/store';

const siteType = z.enum(['Transporter', 'Generator', 'Tsdf', 'Broker']);
/**
 * The EPA Quicker Sign schema
 */
const _quickerSignatureSchema = z.object({
  siteId: z.string(),
  siteType: siteType,
  transporterOrder: z.number().optional(),
  printedSignatureName: z.string(),
  printedSignatureDate: z.string(),
  manifestTrackingNumbers: z.string().array(),
});

const _quickerSignDataSchema = z.object({
  handler: z.any(),
  siteType: z.enum(['Generator', 'Transporter', 'Tsdf']),
});

export type QuickerSignData = z.infer<typeof _quickerSignDataSchema>;
export type QuickerSignature = z.infer<typeof _quickerSignatureSchema>;

interface QuickerSignProps {
  mtn: string[];
  mtnHandler: Handler | Transporter;
  siteType: RcraSiteType;
  handleClose?: () => void;
}

/**
 * Form used to collect signature information, following the RCRAInfo QuickerSignature schema,
 * which can sent to EPA's RCRAInfo to electronically sign manifests.
 * @param mtn
 * @param mtnHandler
 * @param handleClose
 * @param siteType
 * @constructor
 */
export function QuickerSignForm({ mtn, mtnHandler, handleClose, siteType }: QuickerSignProps) {
  const dispatch = useAppDispatch();
  // const user = useAppSelector(selectCurrentUser);
  const [signManifest, { data, error: ApiError }] = useSignEManifestMutation();
  const [taskId, setTaskId] = useState<string | undefined>(undefined);
  useProgressTracker({ taskId: taskId });
  const { register, handleSubmit, setValue } = useForm<QuickerSignature>({
    defaultValues: {
      printedSignatureName: 'Dude!',
      printedSignatureDate: new Date().toISOString().slice(0, -8),
    },
  });
  const navigate = useNavigate();
  if (!handleClose) {
    handleClose = () => navigate(-1);
  }

  useEffect(() => {
    if (data?.taskId) {
      dispatch(
        addTask({
          taskId: data.taskId,
          status: 'PENDING',
          taskName: `Signing manifest ${mtn}`,
        })
      );
      setTaskId(data.taskId);
    }
  }, [data]);

  useEffect(() => {
    if (ApiError && taskId) {
      dispatch(
        updateTask({
          taskId: taskId,
          status: 'FAILURE',
        })
      );
    }
  }, [ApiError]);

  const onSubmit: SubmitHandler<QuickerSignature> = (data) => {
    let signature: QuickerSignature = {
      printedSignatureDate: data.printedSignatureDate + '.000Z',
      printedSignatureName: data.printedSignatureName,
      siteId: mtnHandler.epaSiteId,
      siteType: siteType,
      manifestTrackingNumbers: mtn,
    };
    if ('order' in mtnHandler) {
      signature = {
        ...signature,
        transporterOrder: mtnHandler.order,
      };
    }
    signManifest(signature);
  };

  return (
    <>
      <HtForm onSubmit={handleSubmit(onSubmit)}>
        <Row>
          <Col>
            <HtForm.Group>
              <HtForm.Label>Printed Name</HtForm.Label>
              <Form.Control
                id="printedSignatureName"
                type="text"
                placeholder="John Doe"
                {...register(`printedSignatureName`)}
              />
            </HtForm.Group>
          </Col>
          <Col>
            <HtForm.Label htmlFor={'printedSignatureDate'}>Signature Date</HtForm.Label>
            <HtForm.InputGroup>
              <Form.Control
                id="printedSignatureDate"
                type="datetime-local"
                {...register(`printedSignatureDate`)}
              />
              <Button
                variant="outline-secondary"
                onClick={() => {
                  setValue('printedSignatureDate', new Date().toISOString().slice(0, -8), {
                    shouldDirty: true,
                  });
                }}
              >
                Now
              </Button>
            </HtForm.InputGroup>
          </Col>
        </Row>
        <Container>
          <Row>
            <h5>
              <i>
                Sign as site <b className="text-info">{`${mtnHandler.epaSiteId}`}</b>
              </i>
            </h5>
            <ListGroup variant="flush">
              {mtn.map((value) => {
                return (
                  <ListGroup.Item key={value}>
                    <FaFileSignature className="text-success" />
                    {` ${value}`}
                  </ListGroup.Item>
                );
              })}
            </ListGroup>
          </Row>
          <Stack direction="horizontal" gap={2} className="d-flex justify-content-end">
            <Button variant="outline-danger" onClick={handleClose}>
              Cancel
            </Button>
            <Button variant="success" type="submit">
              <span>Submit Signature </span>
              <FaPen />
            </Button>
          </Stack>
        </Container>
      </HtForm>
    </>
  );
}
