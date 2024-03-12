// Haztrak API - RTK Query
import type { AppDispatch, AppStore, RootState } from './rootStore';

// Root Store
export { rootStore, setupStore, useAppDispatch, useAppSelector } from './rootStore';
export type { RootState, AppDispatch, AppStore };

// Notification Slice
export {
  addTask,
  addAlert,
  removeTask,
  removeAlert,
  updateTask,
  selectTask,
  selectTaskCompletion,
  selectAllTasks,
  selectAllAlerts,
} from './notificationSlice/notification.slice';
export type { LongRunningTask, HaztrakAlert } from './notificationSlice/notification.slice';

// Error Slice
export { addError, selectAllErrors } from './errorSlice/error.slice';

// Authentication Slice
export {
  selectUser,
  selectUserName,
  setCredentials,
  selectAuthenticated,
  removeCredentials,
} from './authSlice/auth.slice';
export type { HaztrakUser } from './authSlice/auth.slice';
