import { useEffect, useRef, useState } from 'react';

/**
 * Hook to set document title
 *
 * @description Can be used to page the title dynamically or just once per page.
 * By default, it reset the title to the previous title when the component using this hook unmounts
 * @param title {string}
 * @param resetOnUnmount {boolean}
 * @param excludeSuffix {boolean}
 */
export function useTitle(title: string, resetOnUnmount = false, excludeSuffix = false) {
  const defaultTitle = useRef(document.title);
  const [dynTitle, setDynTitle] = useState<string | undefined>(undefined);

  useEffect(() => {
    document.title = `${title}${excludeSuffix ? '' : ' | Haztrak'}`;
  }, [excludeSuffix, title]);

  useEffect(() => {
    if (typeof dynTitle === 'string')
      document.title = `${dynTitle}${excludeSuffix ? '' : ' | Haztrak'}`;
  }, [dynTitle, excludeSuffix]);

  useEffect(
    // run on unmount
    () => () => {
      if (!resetOnUnmount) {
        document.title = defaultTitle.current;
      }
    },
    [resetOnUnmount]
  );
  return [dynTitle, setDynTitle] as const;
}