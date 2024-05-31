import { faFloppyDisk } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { ButtonProps } from 'react-bootstrap';
import { HtButton } from '~/components/UI';
import { useReadOnly } from '~/hooks/manifest';

interface ManifestSaveBtnProps extends ButtonProps {}

export function ManifestSaveBtn({ ...props }: ManifestSaveBtnProps) {
  const [readOnly] = useReadOnly();
  if (readOnly) return <></>;
  return (
    <HtButton variant="success" type="submit" name="save" {...props}>
      <span>Save </span>
      <FontAwesomeIcon icon={faFloppyDisk} />
    </HtButton>
  );
}
