import React from 'react';
import { useAuth } from '../AuthProvider';
import styles from './Logout.module.css';

const Logout = () => {
  const { logout } = useAuth();

  const handleLogout = () => {
    logout();
  };

  return (
    <div className={styles['logout-form']}>
      <div className={styles.form}>
        <h2>Are you sure you want to logout?</h2>
        <button onClick={handleLogout}>Logout</button>
      </div>
    </div>
  );
};

export default Logout;
