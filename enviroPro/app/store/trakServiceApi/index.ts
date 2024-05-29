import { trakServiceApi } from './trakServiceApi';
import { userApi } from './userApi';

export const { useGetTaskStatusQuery } = trakServiceApi;
export const {
  useLoginMutation,
  useGetUserQuery,
  useGetProfileQuery,
  useGetRcrainfoProfileQuery,
  useUpdateUserMutation,
} = userApi;
