import React from 'react';
import { useAuth } from './AuthProvider';

const Logout = () => {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
  };

  return (
    <div className='logout-form'>
      <div className='form'>
        <h2>Are you sure you want to logout?</h2>
        <button onClick={handleLogout}>Logout</button>
      </div>
    </div>
  );
};

export default Logout;
