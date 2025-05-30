import React, { createContext, Dispatch, SetStateAction, useState } from 'react';
import { LoaderFunction, Outlet } from 'react-router';
import { ToastContainer } from 'react-toastify';
import { ErrorBoundary } from '~/components/Error';
import { Notifications } from '~/components/Notifications/Notifications';
import { rootStore as store } from '~/store';
import { haztrakApi } from '~/store/htApi.slice';
import { Sidebar } from './Sidebar/Sidebar';
import { TopNav } from './TopNav/TopNav';

export interface NavContextProps {
  showSidebar: boolean;
  setShowSidebar: Dispatch<SetStateAction<boolean>>;
}

export const NavContext = createContext<NavContextProps>({
  showSidebar: false,
  setShowSidebar: () => console.warn('no showSidebar context'),
});

export const rootLoader: LoaderFunction = async () => {
  const query = store.dispatch(haztrakApi.endpoints.getOrgs.initiate());

  return query
    .unwrap()
    .catch((_err) => null)
    .finally(() => query.unsubscribe());
};

export function Root() {
  const [showSidebar, setShowSidebar] = useState(false);
  return (
    <NavContext.Provider value={{ showSidebar, setShowSidebar }}>
      <TopNav />
      <Sidebar />
      <main className="tw:mx-8 tw:mt-20">
        <ToastContainer
          position="bottom-right"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop
          closeOnClick
          pauseOnHover
          limit={3}
        />
        <Notifications />
        <ErrorBoundary>
          <Outlet />
        </ErrorBoundary>
      </main>
    </NavContext.Provider>
  );
}
