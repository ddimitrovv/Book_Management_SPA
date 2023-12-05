import React, { createContext, useState, useContext } from 'react';
import paths from '../appPaths/paths';
import urls from '../appPaths/urls';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(() => {
    // Check local storage for authentication state
    const storedAuthState = localStorage.getItem('authState');
    return storedAuthState ? JSON.parse(storedAuthState) : false;
  });
  const navigate = useNavigate();

  const login = async (username, password, navigate) => {
    try {
      const response = await fetch(urls.Login, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const data = await response.json();
      const authToken = data.token;
      console.log(data);

      localStorage.setItem('authToken', authToken);
      localStorage.setItem('authState', JSON.stringify(true));
      localStorage.setItem('username', username);

      setIsAuthenticated(true);
      navigate(paths.Home);
    } catch (error) {
      console.error('Login error:', error.message);
    }
  };

  const logout = async () => {
    try {
      const authToken = localStorage.getItem('authToken');

      const response = await fetch(urls.Logout, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        },
      });

      if (!response.ok) {
        throw new Error('Logout failed');
      }

      localStorage.removeItem('authToken');
      localStorage.removeItem('authState');
      localStorage.removeItem('username')

      setIsAuthenticated(false);
      navigate(paths.Home);

    } catch (error) {
      console.error('Logout error:', error.message);
    }
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

const useAuth = () => {
  const authContext = useContext(AuthContext);

  if (!authContext) {
    throw new Error('useAuth must be used within an AuthProvider');
  }

  return authContext;
};

export { AuthProvider, useAuth, AuthContext };
