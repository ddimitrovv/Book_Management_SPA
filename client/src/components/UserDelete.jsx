import React from 'react';
import urls from '../appPaths/urls';
import paths from '../appPaths/paths';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthProvider';

const UserDelete = () => {

  const { logout } = useAuth();
  const authToken = localStorage.getItem('authToken');
  const navigate = useNavigate();

  const handleDeleteUser = () => {

    const headers = authToken
      ? {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        }
      : { 'Content-Type': 'application/json' };

    fetch(urls.DeleteUser, {
      method: 'DELETE',
      headers: headers,
    })
    .then(response => {
      if (response.status !== 204) {
        throw new Error(`${response.status} (${response.statusText})`);
      }
    })
    .then(() => {
      logout();
      navigate(paths.Home);
    })
    .catch(error => {
      console.error('Error deleting book:', error.message);
    });
  };

  return (
    <div className='logout-form'>
      <div className='form'>
        <h2>Are you sure you want to detele your profile?</h2>
        <button onClick={handleDeleteUser}>Delete</button>
      </div>
    </div>
  );
};

export default UserDelete;
