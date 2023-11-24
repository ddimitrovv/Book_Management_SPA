import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './AuthProvider';
import paths from '../appPaths/paths';

const Navigation = () => {
  const { isAuthenticated } = useAuth();

  return (
    <nav>
      <ul role='list'>
        {!isAuthenticated ? (
          <li>
            <Link to={paths.Login}>Login</Link>
          </li>
        ) : (
          <>
            <li>
              <p>Wellcome, {localStorage.getItem('username')}</p>
              <Link to={paths.Home}>Home</Link>
            </li>
            <li>
              <Link to={paths.Logout}>Logout</Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navigation;