import { selectCurrentUser, useAppSelector, useGetUserQuery, useLoginMutation } from '~/store';

export const useAuth = () => {
  // ToDo: add user loading state
  useGetUserQuery();
  const user = useAppSelector(selectCurrentUser);
  const [login, loginState] = useLoginMutation();

  return {
    user,
    login: { login, ...loginState },
  };
};
