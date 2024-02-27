import { useParams } from 'react-router';

export default function ManifestDetails() {
  const { siteId, mtn } = useParams();
  return (
    <h1>
      Site {siteId} manifests {mtn}
    </h1>
  );
}
