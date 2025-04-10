import { DropdownMenuSeparator } from '@radix-ui/react-dropdown-menu';
import { LogOut } from 'lucide-react';
import React, { useContext } from 'react';
import { LuMenu, LuUser } from 'react-icons/lu';
import { TbBinaryTree } from 'react-icons/tb';
import { Link } from 'react-router';
import { OrgSelect } from '~/components/Org/OrgSelect';
import { Avatar, AvatarFallback, AvatarImage, Button } from '~/components/ui';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '~/components/ui/DropDown/dropdown-menu';
import { NavContext, NavContextProps } from '~/features/layout/Root';
import logo from '/assets/img/haztrak-logos/haztrak-logo-zip-file/svg/logo-no-background.svg';

import { FaUser } from 'react-icons/fa';
import { useGetProfileQuery, useLogoutMutation } from '~/store';

export function TopNav() {
  const { showSidebar, setShowSidebar } = useContext<NavContextProps>(NavContext);
  const [logout] = useLogoutMutation();
  const { data: profile } = useGetProfileQuery();

  const handleLogout = () => {
    logout();
  };

  const toggleSidebar = () => {
    setShowSidebar(!showSidebar);
  };

  return (
    <header className="tw:fixed tw:left-0 tw:top-0 tw:z-50 tw:flex tw:min-h-16 tw:w-full tw:items-center tw:bg-primary tw:px-5">
      <nav className="tw:flex tw:grow tw:items-center tw:justify-between">
        <div className="tw:flex tw:items-center" id="leftNavSection">
          <Button
            size="icon"
            aria-label="toggleSidebarNavigation"
            aria-hidden={false}
            id="sidebarToggle"
            onClick={toggleSidebar}
            rounded
            variant={null}
            className="tw:border-none tw:bg-transparent tw:text-white tw:hover:bg-gray-700"
          >
            <LuMenu size={32} strokeWidth={2} />
          </Button>
          <Link to="/" className="tw:hidden tw:px-3 tw:sm:block">
            <img
              src={logo}
              alt="haztrak logo, hazardous waste tracking made easy."
              width={125}
              height={'auto'}
              className="tw:my-3"
            />
          </Link>
        </div>
        <div
          className="tw:hidden tw:max-w-64 tw:grow tw:items-center tw:justify-center tw:md:flex"
          id="centerNavSection"
        >
          <OrgSelect />
        </div>
        <div id="rightNavSection" className="tw:flex tw:items-center">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                variant="outline"
                className="tw:border-0 tw:text-white tw:hover:bg-transparent tw:hover:text-accent"
              >
                <Avatar>
                  <AvatarImage src={profile?.avatar} alt="avatar" />
                  <AvatarFallback>
                    <FaUser size={16} className="tw:text-black" />
                  </AvatarFallback>
                </Avatar>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="tw:me-5 tw:w-56">
              <DropdownMenuItem asChild>
                <Link to={'./profile'} relative="path">
                  <LuUser className="tw:mr-2 tw:size-4 tw:text-primary" />
                  <span>Profile</span>
                </Link>
              </DropdownMenuItem>
              <DropdownMenuItem asChild>
                <Link to={'./organization'} relative="path">
                  <TbBinaryTree className="tw:mr-2 tw:size-4 tw:text-primary" />
                  <span>Organization</span>
                </Link>
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem onClick={handleLogout}>
                <LogOut className="tw:mr-2 tw:size-4 tw:text-destructive" />
                <span>Log out</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </nav>
    </header>
  );
}
