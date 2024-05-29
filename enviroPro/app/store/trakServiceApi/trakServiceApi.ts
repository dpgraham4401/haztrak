import { BaseQueryFn } from '@reduxjs/toolkit/query';
import { createApi } from '@reduxjs/toolkit/query/react';
import axios, {
  AxiosError,
  AxiosRequestConfig,
  AxiosResponse,
  InternalAxiosRequestConfig,
} from 'axios';

import { rootStore } from '~/store';

export interface TaskStatus {
  status: 'PENDING' | 'STARTED' | 'SUCCESS' | 'FAILURE' | 'NOT FOUND';
  taskId: string;
  taskName: string;
  createdDate?: string;
  doneDate?: string;
  result?: any;
}

/** An Axios instance with an interceptor to automatically apply authentication headers*/
const trakService = axios.create({
  baseURL: `${import.meta.env.VITE_HT_API_URL}/api`,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

/**interceptor to apply auth token from redux store*/
trakService.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    config.headers = config.headers ?? {};
    const token = rootStore.getState().auth.token;
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export interface HtApiQueryArgs {
  url: string;
  method: AxiosRequestConfig['method'];
  data?: AxiosRequestConfig['data'];
  params?: AxiosRequestConfig['params'];
}

export interface HtApiError extends AxiosError {
  data?: AxiosResponse['data'];
  statusText?: string;
}

/**
 * Used by the RTK Query createApi, so we can hook into our htApi service
 * for user authentication between the client and server.
 *
 * For information on custom RTK baseQuery types, see:
 * https://redux-toolkit.js.org/rtk-query/usage-with-typescript#typing-a-basequery
 * @param baseUrl
 */
export const trakServiceApiBaseQuery =
  (
    { baseUrl }: { baseUrl: string } = { baseUrl: '/' }
  ): BaseQueryFn<
    HtApiQueryArgs, // Args
    unknown, // Result
    HtApiError // Error
  > =>
  async ({ url, method, data, params }) => {
    try {
      const response = await trakService({ url: baseUrl + url, method, data, params });
      return { data: response.data };
    } catch (axiosError) {
      const err = axiosError as AxiosError;
      return {
        error: {
          statusText: err.response?.statusText,
          data: err.response?.data || err.message,
        } as HtApiError,
      };
    }
  };

export const trakServiceApi = createApi({
  tagTypes: ['user', 'auth', 'profile', 'rcrainfoProfile', 'site', 'code', 'manifest'],
  reducerPath: 'haztrakApi',
  baseQuery: trakServiceApiBaseQuery({
    baseUrl: `${import.meta.env.VITE_HT_API_URL}/api/`,
  }),
  endpoints: (build) => ({
    // Note: build.query<ReturnType, ArgType>
    // searchRcrainfoSites: build.query<Array<RcraSite>, RcrainfoSiteSearch>({
    //   query: (data: RcrainfoSiteSearch) => ({
    //     url: 'rcra/handler/search',
    //     method: 'post',
    //     data: data,
    //   }),
    // }),
    // searchRcraSites: build.query<Array<RcraSite>, RcrainfoSiteSearch>({
    //   query: (data: RcrainfoSiteSearch) => ({
    //     url: 'rcra/site/search',
    //     method: 'get',
    //     params: { epaId: data.siteId, siteType: data.siteType },
    //   }),
    // }),
    // getRcrainfoSite: build.query<RcraSite, string | null>({
    //   query: (epaSiteId) => ({
    //     url: `rcra/handler/${epaSiteId}`,
    //     method: 'get',
    //   }),
    // }),
    getTaskStatus: build.query<TaskStatus, string>({
      query: (taskId) => ({ url: `task/${taskId}`, method: 'get' }),
    }),
    // getFedWasteCodes: build.query<Array<Code>, void>({
    //   query: () => ({ url: 'rcra/waste/code/federal', method: 'get' }),
    //   providesTags: ['code'],
    // }),
    // getStateWasteCodes: build.query<Array<Code>, string>({
    //   query: (state) => ({ url: `rcra/waste/code/state/${state}`, method: 'get' }),
    //   providesTags: ['code'],
    // }),
    // getDotIdNumbers: build.query<Array<string>, string>({
    //   query: (id) => ({ url: 'rcra/waste/dot/id', method: 'get', params: { q: id } }),
    //   providesTags: ['code'],
    // }),
    // getOrgSites: build.query<Array<HaztrakSite>, string>({
    //   query: (id) => ({ url: `org/${id}/sites`, method: 'get' }),
    //   providesTags: ['site'],
    // }),
    // getUserHaztrakSites: build.query<Array<HaztrakSite>, void>({
    //   query: () => ({ url: 'site', method: 'get' }),
    //   providesTags: ['site'],
    // }),
    // getUserHaztrakSite: build.query<HaztrakSite, string>({
    //   query: (epaId) => ({ url: `site/${epaId}`, method: 'get' }),
    //   providesTags: ['site'],
    // }),
    //   getMTN: build.query<Array<MtnDetails>, string | undefined>({
    //     query: (siteId) => ({
    //       url: siteId ? `rcra/manifest/mtn/${siteId}` : 'rcra/manifest/mtn',
    //       method: 'get',
    //     }),
    //     providesTags: ['manifest'],
    //   }),
    //   getManifest: build.query<Manifest, string>({
    //     query: (mtn) => ({ url: `rcra/manifest/${mtn}`, method: 'get' }),
    //     providesTags: ['manifest'],
    //   }),
    //   createManifest: build.mutation<Manifest, Manifest>({
    //     query: (data) => ({
    //       url: 'rcra/manifest',
    //       method: 'POST',
    //       data,
    //     }),
    //     invalidatesTags: ['manifest'],
    //   }),
    //   updateManifest: build.mutation<Manifest, { mtn: string; manifest: Manifest }>({
    //     query: ({ mtn, manifest }) => ({
    //       url: `rcra/manifest/${mtn}`,
    //       method: 'PUT',
    //       data: manifest,
    //     }),
    //     invalidatesTags: ['manifest'],
    //   }),
    //   saveEManifest: build.mutation<TaskResponse, Manifest>({
    //     query: (data) => ({
    //       url: 'rcra/manifest/emanifest',
    //       method: 'POST',
    //       data,
    //     }),
    //     invalidatesTags: ['manifest'],
    //   }),
    //   syncEManifest: build.mutation<TaskResponse, string>({
    //     query: (siteId) => ({
    //       url: 'rcra/manifest/emanifest/sync',
    //       method: 'POST',
    //       data: { siteId: siteId },
    //     }),
    //     invalidatesTags: ['manifest'],
    //   }),
    //   signEManifest: build.mutation<TaskResponse, QuickerSignature>({
    //     query: (signature) => ({
    //       url: 'rcra/manifest/emanifest/sign',
    //       method: 'POST',
    //       data: signature,
    //     }),
    //     invalidatesTags: ['manifest'],
    //   }),
  }),
});
