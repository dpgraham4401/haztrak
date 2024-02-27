import { useParams } from 'react-router';

export default function SiteDetails() {
  const { siteId } = useParams();
  return <h1>Site ID {siteId}</h1>;
}
