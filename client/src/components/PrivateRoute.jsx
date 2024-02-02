import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from './AuthProvider';
import paths from '../appPaths/paths';

const PrivateRoute = ({ element, ...rest }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  return isAuthenticated ? (
    element
  ) : (
    <Navigate to={paths.Login} replace state={{ from: rest.location }} />
  );
};

export default PrivateRoute;
