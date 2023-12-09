import React, { useEffect, useState } from 'react';
import { Carousel } from 'react-bootstrap';
import { useAuth } from './AuthProvider';
import urls from '../appPaths/urls';
import paths from '../appPaths/paths';
import Card from './BookCard';

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
      <h1>Welcome to Your Library</h1>
      <div>
        {data.books_by_genre && Object.keys(data.books_by_genre).length > 0 ? (
          <div className="scrollable-container">
            {Object.entries(data.books_by_genre).map(([genre, books], index) => (
              <div key={index} className="genre-section">
                <h2>{genre}</h2>
                <div className="book-row">
                  {books.map((book, bookIndex) => (
                    <Card key={bookIndex} book={book} />
                  ))}
                </div>
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