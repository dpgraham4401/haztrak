import { useParams } from 'react-router';

export default function Manifests() {
  const { siteId } = useParams();
  return <h1>Site {siteId} manifests</h1>;
}
