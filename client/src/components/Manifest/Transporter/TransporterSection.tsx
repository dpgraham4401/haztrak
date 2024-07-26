import { ErrorMessage } from '@hookform/error-message';
import { Manifest, Transporter } from 'src/components/Manifest/manifestSchema';
import { TransporterTable } from 'src/components/Manifest/Transporter/TransporterTable';
import { HtButton } from 'src/components/UI';
import { useReadOnly } from 'src/hooks/manifest';
import { useHandlerSearchConfig } from 'src/hooks/manifest/useOpenHandlerSearch/useHandlerSearchConfig';
import { Alert } from 'react-bootstrap';
import { useFieldArray, useFormContext } from 'react-hook-form';
import { v4 as uuidv4 } from 'uuid';

interface TransporterSectionProps {
  setupSign: () => void;
}

export function TransporterSection({ setupSign }: TransporterSectionProps) {
  const [, setSearchConfigs] = useHandlerSearchConfig();
  const [readOnly] = useReadOnly();
  const manifestForm = useFormContext<Manifest>();
  const { errors } = manifestForm.formState;
  const transporterForm = useFieldArray<Manifest, 'transporters'>({
    control: manifestForm.control,
    name: 'transporters',
  });
  const transporters = manifestForm.watch('transporters');

  transporters.forEach((transporter, index) => {
    if (!transporter.clientKey) {
      // @ts-ignore
      manifestForm.setValue(`transporters[${index}].clientKey`, uuidv4());
    }
  });

  return (
    <>
      <TransporterTable
        transporters={transporters}
        arrayFieldMethods={transporterForm}
        setupSign={setupSign}
      />
      {readOnly ? (
        <></>
      ) : (
        <HtButton
          onClick={() => {
            setSearchConfigs({ siteType: 'transporter', open: true });
          }}
          children={'Add Transporter'}
          variant="outline-primary"
          horizontalAlign
        />
      )}
      <ErrorMessage
        errors={errors}
        name={'transporters'}
        render={({ message }) => (
          <Alert variant="danger" className="text-center m-3">
            {message}
          </Alert>
        )}
      />
    </>
  );
}
