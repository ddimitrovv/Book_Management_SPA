import React, { useEffect, useState } from 'react';
import { Carousel } from 'react-bootstrap';
import { useAuth } from '../AuthProvider';
import urls from '../../appPaths/urls';
import paths from '../../appPaths/paths';
import Card from '../BookCard/BookCard';
import styles from './Home.module.css';

export default function Home() {
  const { isAuthenticated } = useAuth();
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      const authToken = localStorage.getItem('authToken');

      const headers = authToken
        ? {
            'Content-Type': 'application/json',
            Authorization: `Token ${authToken}`,
          }
        : { 'Content-Type': 'application/json' };

      fetch(urls.Home, {
        method: 'GET',
        headers: headers,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to fetch data');
          }
          return response.json();
        })
        .then((responseData) => {
          setData(responseData);
        })
        .catch((error) => {
          console.error('Error fetching data:', error.message);
        });
    };
    fetchData();
  }, [isAuthenticated]);

  return (
    <div>
      <div className={styles.heroSection}>
        <h1 className={styles.welcome}>Welcome to BookManagement</h1>
        <h2 className={styles.welcomeMessage}>
          Your Gateway to Knowledge and Imagination! Dive into the world of books, where every page holds a new adventure, and every story sparks the imagination. Discover, learn, and embark on a literary journey with us. Happy Reading!
        </h2>
      </div>
      <div>
        {data.books_by_genre && Object.keys(data.books_by_genre).length > 0 ? (
          <div className={styles.scrollableContainer}>
            {Object.entries(data.books_by_genre).map(([genre, books], index) => (
              <div key={index} className={styles.genreSection}>
                <h2 className={styles.booksGenre}>{genre}</h2>
                <div className={styles.bookRow}>
                  {books.map((book, bookIndex) => (
                    <Card key={bookIndex} book={book} />
                  ))}
                </div>
                <hr />
              </div>
            ))}
          </div>
        ) : (
          <p>No books data available</p>
        )}
      </div>
    </div>
  );
}