import { ThunkAction, UnknownAction } from '@reduxjs/toolkit';
import { useCallback, useEffect, useState } from 'react';
import {
  selectTask,
  selectTaskCompletion,
  TaskStatus,
  updateTask,
  useAppDispatch,
  useAppSelector,
  useGetTaskStatusQuery,
} from '~/store';

interface UseProgressTrackerConfig {
  taskId: string | undefined;
  reduxAction?: UnknownAction | ThunkAction<any, any, any, any>;
  pollingInterval?: number;
  showMessages?: boolean;
}

interface TaskStatusResponse<T> extends Omit<TaskStatus, 'result'> {
  result: T;
}

interface UseProgressTrackerReturn<T> {
  data?: TaskStatusResponse<T>;
  inProgress: boolean;
  error?: any;
}

/**
 * useProgressTracker hook tracks the progress of a long-running task on the server
 * optionally dispatches a redux action or async thunk after the task completes
 */
export function useProgressTracker<T>({
  taskId,
  reduxAction,
  pollingInterval,
}: UseProgressTrackerConfig): UseProgressTrackerReturn<T> {
  const dispatch = useAppDispatch();
  const taskComplete = useAppSelector(selectTaskCompletion(taskId));
  const [inProgress, setInProgress] = useState<boolean>(taskId !== undefined);
  const [data, setData] = useState<TaskStatusResponse<T> | undefined>(undefined);
  const [error, setError] = useState<any | undefined>(
    useAppSelector(selectTask(taskId))?.status === 'FAILURE'
  );

  const failTask = useCallback(
    (queryError: any) => {
      setInProgress(false);
      dispatch(updateTask({ taskId: taskId, status: 'FAILURE', complete: true }));
      setError('Task failed');
      setError(queryError ?? 'Task failed');
    },
    [dispatch, taskId]
  );

  // @ts-expect-error - We skip the query if taskId is undefined
  const { data: queryData, error: queryError } = useGetTaskStatusQuery(taskId, {
    pollingInterval: pollingInterval ?? 3000,
    skip: !inProgress || taskId === undefined,
  });

  // If we get a response from the server, update the task status
  useEffect(() => {
    if (queryData) {
      if (queryData.status === 'SUCCESS') {
        setData(queryData as TaskStatusResponse<T>);
        setInProgress(false);
        dispatch(updateTask({ ...queryData, taskId: taskId, complete: true }));
      } else if (queryData?.status === 'FAILURE') {
        failTask(queryData);
      } else {
        setInProgress(true);
        dispatch(updateTask({ ...queryData, taskId: taskId }));
      }
    }
  }, [dispatch, failTask, queryData, taskId]);

  useEffect(() => {
    if (queryError) {
      failTask(queryError);
    }
  }, [failTask, queryError]);

  // If taskId defined, the task is not set to complete, mark inProgress as true
  useEffect(() => {
    if (!inProgress && !taskComplete && taskId !== undefined) {
      setInProgress(true);
    }
  }, [inProgress, taskComplete, taskId]);

  useEffect(() => {
    if (taskComplete) {
      if (reduxAction) dispatch(reduxAction);
      setInProgress(false);
    }
  }, [dispatch, reduxAction, taskComplete, taskId]);

  return { data, inProgress, error } as const;
}
