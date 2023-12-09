import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './AuthProvider';
import paths from '../appPaths/paths';

const Navigation = () => {
  const { isAuthenticated } = useAuth();
  const isHomePage = window.location.pathname == '/';
  
  return (
    <nav className='navigation'>
      <ul role='list' className='nav-links'>
        {!isAuthenticated ? (
          <>
            <li>
              <Link to={paths.Login}>Login</Link>
            </li>
            <li>
              <Link to={paths.Register}>Register</Link>
            </li>
          </>
        ) : (
          <>
            <li>
              <Link to={paths.UserDetails}>{localStorage.getItem('username')}</Link>
            </li>
            {isHomePage ? (
              <>
                <li>
                  <Link to={paths.MyBooks}>My Books</Link>
                </li>
                <li>
                  <Link to={paths.Logout}>Logout</Link>
                </li>                
              </>
            ) : (
              <>
                <li>
                  <Link to={paths.Home}>Home</Link>
                </li>
                <li>
                  <Link to={paths.Logout}>Logout</Link>
                </li>
              </>
            )}
          </>
        )}
      </ul>
    </nav>
  );
  
};

export default Navigation;