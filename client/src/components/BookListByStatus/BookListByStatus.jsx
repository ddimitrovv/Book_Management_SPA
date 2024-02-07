import React, { useEffect, useState } from 'react';
import { useParams, useSearchParams } from 'react-router-dom';
import urls from '../../appPaths/urls';
import BookCard from '../BookCard/BookCard';
import styles from './BookListByStatus.module.css';

export default function BookListByStatus() {

  const { status } = useParams();
  const [books, setBooks] = useState([]);
  const [searchParams, setSearchParams] = useSearchParams();
  const [pagination, setPagination] = useState({
    next: null,
    previous: null,
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const authToken = localStorage.getItem('authToken');
        const headers = authToken
          ? {
              'Content-Type': 'application/json',
              Authorization: `Token ${authToken}`,
            }
          : { 'Content-Type': 'application/json' };

        const response = await fetch(`${urls.BooksByStatus(status)}`, {
          method: 'GET',
          headers: headers,
        });

        if (!response.ok) {
          throw new Error('Failed to fetch books');
        }
        
        const responseData = await response.json();
        setBooks(responseData.results);
        setPagination({
          next: responseData.next,
          previous: responseData.previous,
        });
      } catch (error) {
        console.error('Error fetching books:', error.message);
      }
    };

    fetchData();
  }, [status]);

  const handlePaginationClick = (url) => {
    const authToken = localStorage.getItem('authToken');
    const headers = authToken
      ? {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        }
      : { 'Content-Type': 'application/json' };

    fetch(url, {
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
        setPagination({
          next: responseData.next,
          previous: responseData.previous,
        });
        const page = url.split('=')[1];
        setSearchParams(page ? {page} : {});
      })
      .catch((error) => {
        console.error('Error fetching books:', error.message);
      });
  };

  return (
    <>
      <div className={styles.bookList}>
        {books.map((book) => (
          <BookCard key={book.id} book={book} />
        ))}
      </div>
      {pagination.previous || pagination.next ? (
        <div className={styles.pagination}>
          <button
            onClick={() => handlePaginationClick(pagination.previous)}
            disabled={!pagination.previous}
          >
            Previous
          </button>
          <button
            onClick={() => handlePaginationClick(pagination.next)}
            disabled={!pagination.next}
          >
            Next
          </button>
        </div>
      ) : null}
    </>
  );
}
