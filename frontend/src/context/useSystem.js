'use client';

import { createContext, useContext, useState, useEffect } from 'react';

const SystemContext = createContext({});

export const useSystem = () => useContext(SystemContext);

export const SystemContextProvider = ({ children }) => {
  const [isAsideOpen, setIsAsideOpen] = useState(false);

  return (
    <SystemContext.Provider
      value={{
        isAsideOpen,
        setIsAsideOpen,
      }}
    >
      {children}
    </SystemContext.Provider>
  );
};
