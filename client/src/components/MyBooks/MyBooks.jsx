import React, { useEffect, useState } from 'react';
import { Link, Route } from 'react-router-dom';
import { useAuth } from '../AuthProvider';
import urls from '../../appPaths/urls';
import paths from '../../appPaths/paths';
import styles from './MyBooks.module.css'

export default function MyBooks() {
  const { isAuthenticated } = useAuth();
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      const authToken = localStorage.getItem('authToken');

      const headers = authToken ? {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      } : {'Content-Type': 'application/json',}

      fetch(urls.MyBooks, {
        method: 'GET',
        headers: headers,
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to fetch data');
          }
          return response.json();
        })
        .then(responseData => {
          setData(responseData);
        })
        .catch(error => {
          console.error('Error fetching data:', error.message);
        });
    };
    fetchData();
  }, [isAuthenticated]);

  return (
    <div className={styles.home}>
      <h1><Link to={paths.AddBook}>Add Book</Link></h1>
        <div className={styles.bookCardWrapper}>
            {data.status && Array.isArray(data.status) ? (
                data.status.map((status, index) => <Card key={index} status={status} />)
            ) : (
                <p>No status data available</p>
            )}
        </div>
    </div>
  );
}


const Card = ({ status }) => {
    const [statusValue, statusLabel] = status;
  
    return (
      <div className={styles.bookCard}>
        <div className={styles.bookCardPicture}>
          <img
            src="https://img.freepik.com/premium-photo/books-collection-isolated-white-background-vector-illustration-retro-style_941097-2684.jpg"
            alt="Book Cover"
          />
        </div>
        <div className={styles.bookCardWrapper}>
          <div className={styles.bookCardInfo}>
            <button className={styles.bookStatusButton}>
              <Link to={paths.BooksByStatus(statusValue)}>
                <h2>{statusValue}</h2>
              </Link>
            </button>
          </div>
        </div>
      </div>
    );
  };
  