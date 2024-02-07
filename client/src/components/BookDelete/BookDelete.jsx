import React from 'react';
import urls from '../../appPaths/urls';
import paths from '../../appPaths/paths';
import { useNavigate, useParams } from 'react-router-dom';
import styles from './BookDelete.module.css';

const BookDelete = () => {

  const { id } = useParams();
  const authToken = localStorage.getItem('authToken');
  const navigate = useNavigate();

  const handleDeleteBook = () => {

    const headers = authToken
      ? {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        }
      : { 'Content-Type': 'application/json' };

    fetch(urls.BookDelete(id), {
      method: 'DELETE',
      headers: headers,
    })
    .then(response => {
      if (response.status !== 204) {
        throw new Error(`${response.status} (${response.statusText})`);
      }
    })
    .then(() => {
      navigate(paths.Home)
    })
    .catch(error => {
      console.error('Error deleting book:', error.message);
    });
  };

  return (
    <div className={styles.deleteBookForm}>
      <div className={styles.form}>
        <h2>Are you sure you want to detele this book?</h2>
        <button onClick={handleDeleteBook}>Delete</button>
      </div>
    </div>
  );
};

export default BookDelete;
