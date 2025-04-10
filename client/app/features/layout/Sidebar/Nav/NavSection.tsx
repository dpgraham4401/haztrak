import { Separator } from '~/components/ui/Separator/Separator';
import { RoutesSection } from '~/features/layout/Sidebar/SidebarRoutes';
import { NavItem } from './NavItem';

interface SidebarSectionProps {
  section: RoutesSection;
}

export function NavSection({ section }: SidebarSectionProps) {
  return (
    <div className="tw:mt-8">
      <Separator />
      <p className="tw:text-primary">{section.name}</p>
      {section.routes.map((route) => {
        return (
          <div key={route.id}>
            <NavItem route={route} />
          </div>
        );
      })}
    </div>
  );
}
