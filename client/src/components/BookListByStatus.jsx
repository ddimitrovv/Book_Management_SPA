// BookListByStatus.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import urls from '../appPaths/urls';
import BookCard from './BookCard';

export default function BookListByStatus() {
  const { status } = useParams();
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      const authToken = localStorage.getItem('authToken');

      const headers = authToken
        ? {
            'Content-Type': 'application/json',
            Authorization: `Token ${authToken}`,
          }
        : { 'Content-Type': 'application/json' };

      fetch(`${urls.BooksByStatus(status)}`, {
        method: 'GET',
        headers: headers,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Failed to fetch books');
          }
          return response.json();
        })
        .then((responseData) => {
          setBooks(responseData.results);
        })
        .catch((error) => {
          console.error('Error fetching books:', error.message);
        });
    };

    fetchData();
  }, [status]);

  return (
    <div className="book-list">
      {books.map((book) => (
        <BookCard key={book.id} book={book} />
      ))}
    </div>
  );
}
