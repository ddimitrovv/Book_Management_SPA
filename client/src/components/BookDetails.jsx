import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import paths from '../appPaths/paths';
import urls from '../appPaths/urls';

export default function BookDetails() {
  const { id } = useParams();
  const authToken = localStorage.getItem('authToken');
  const [bookDetails, setBookDetails] = useState();

  useEffect(() => {
    fetch(urls.BookDetail(id), {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      },
    })
      .then(response => response.json())
      .then(data => {
        setBookDetails(data);
      })
      .catch(error => {
        console.error('Error fetching user details:', error.message);
      });
  }, [id, authToken]);

  if (!bookDetails) {
    return <p>Loading...</p>;
  }

  return (
    <div className="book-details">
      <div className="book-details-header">
        <h2>{bookDetails.name}</h2>
        <p>{bookDetails.author}</p>
      </div>
      <div className="book-details-content">
        <div className="profile-picture">
          {bookDetails.picture ? (
            <img src={bookDetails.picture} alt={`Book Cover`} />
          ) : (
            <img src="https://nnpdev.wustl.edu/img/bookCovers/genericBookCover.jpg" alt="Book Cover" />
          )}
        </div>
        <div className="book-description">
          <p>{bookDetails.description}</p>
        </div>
      </div>
      <div className="book-details-footer">
        <button><Link to={paths.BooksByStatus}>Back to List</Link></button>
      </div>
    </div>
  );
};