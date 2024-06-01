import { trakServiceApi } from './trakServiceApi';
import { userApi } from './userApi';

export type { TaskStatus } from './trakServiceApi';

export const {
  useGetDotIdNumbersQuery,
  useLazyGetDotIdNumbersQuery,
  useGetStateWasteCodesQuery,
  useSearchRcrainfoSitesQuery,
  useSearchRcraSitesQuery,
  useGetUserHaztrakSitesQuery,
  useGetUserHaztrakSiteQuery,
  useSaveEManifestMutation,
  useSyncEManifestMutation,
  useUpdateManifestMutation,
  useCreateManifestMutation,
  useGetRcrainfoSiteQuery,
  useGetOrgSitesQuery,
  useGetTaskStatusQuery,
  useSignEManifestMutation,
  useGetFedWasteCodesQuery,
} = trakServiceApi;
export { trakServiceApi };
export const {
  useLoginMutation,
  useGetUserQuery,
  useGetProfileQuery,
  useGetRcrainfoProfileQuery,
  useUpdateUserMutation,
  useUpdateRcrainfoProfileMutation,
  useSyncRcrainfoProfileMutation,
} = userApi;
export { userApi };
export type {
  ProfileSlice,
  LoginRequest,
  LoginResponse,
  HaztrakProfileOrg,
  HaztrakProfileSite,
  RcrainfoProfileSite,
  HaztrakProfileResponse,
  RcrainfoProfile,
  HaztrakSitePermissions,
  RcrainfoProfileState,
  RcrainfoSitePermissions,
  HaztrakModulePermissions,
} from './userApi';
