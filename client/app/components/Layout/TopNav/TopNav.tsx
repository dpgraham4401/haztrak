import logo from '/assets/img/haztrak-logos/haztrak-logo-zip-file/svg/logo-no-background.svg';
import { faArrowRightFromBracket, faBars, faGear, faUser } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import React, { useContext } from 'react';
import { Button, Col, Dropdown, Row } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { NavContext, NavContextProps } from '~/components/Layout/Root';
import { OrgSelect } from '~/components/Org/OrgSelect';
import { useLogoutMutation } from '~/store';

export function TopNav() {
  const { showSidebar, setShowSidebar } = useContext<NavContextProps>(NavContext);
  const [logout] = useLogoutMutation();

  const handleLogout = () => {
    logout();
  };

  const toggleSidebar = () => {
    setShowSidebar(!showSidebar);
  };

  return (
    <nav className="sb-topnav navbar navbar-expand navbar-dark bg-dark d-flex">
      <div className="flex-grow-1">
        <Row className="align-items-center">
          <Col xs={12} md={5}>
            <Button
              aria-label="toggleSidebarNavigation"
              aria-hidden={false}
              id="sidebarToggle"
              onClick={toggleSidebar}
              variant="dark"
              className="mx-3 rounded-circle btn-hover-dark"
            >
              <FontAwesomeIcon icon={faBars} />
            </Button>
            <Link to="/" className="p-3 ">
              <img
                src={logo}
                alt="haztrak logo, hazardous waste tracking made easy."
                width={125}
                height={'auto'}
                className="my-3"
              />
            </Link>
          </Col>
          <Col md={5} className="me-5 d-none d-md-block">
            <OrgSelect />
          </Col>
        </Row>
      </div>
      <ul className="navbar-nav ms-auto ms-md-0 me-3 me-lg-4 btn-hover-dark rounded-circle">
        <li className="nav-item dropdown">
          <Dropdown>
            <Dropdown.Toggle
              aria-label="userProfileDropDown"
              aria-hidden={false}
              id="navbarDropdown"
              className="nav-link bg-transparent btn-dark btn-outline-none"
            >
              <FontAwesomeIcon icon={faUser} />
            </Dropdown.Toggle>
            <Dropdown.Menu>
              <Dropdown.Item as={Link} to="settings/">
                <FontAwesomeIcon icon={faGear} className="pe-2 text-primary" />
                Settings
              </Dropdown.Item>
              <Dropdown.Item as={Link} to="profile/">
                <FontAwesomeIcon icon={faUser} className="pe-2 text-primary" />
                Profile
              </Dropdown.Item>
              <hr className="dropdown-divider" />
              <Dropdown.Item onClick={handleLogout}>
                <FontAwesomeIcon icon={faArrowRightFromBracket} className="pe-2 text-danger" />
                Logout
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
        </li>
      </ul>
    </nav>
  );
}
