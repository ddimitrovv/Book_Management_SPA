import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import paths from '../appPaths/paths';
import urls from '../appPaths/urls';
import StarRating from './StarRating';
import rateBook from '../operations/rateBook';

export default function BookDetails() {
  const { id } = useParams();
  const authToken = localStorage.getItem('authToken');
  const [bookDetails, setBookDetails] = useState();
  const [isUserAuth, setIsUserAuth] = useState();
  const [userRating, setUserRating] = useState();

  useEffect(() => {
    const headers = authToken
        ? {
            'Content-Type': 'application/json',
            Authorization: `Token ${authToken}`,
          }
        : { 'Content-Type': 'application/json' };

    fetch(urls.BookDetail(id), {
      method: 'GET',
      headers: headers
    })
      .then(response => response.json())
      .then(data => {
        setBookDetails(data.book);
        setIsUserAuth(data.is_auth);
        setUserRating(data.user_rating);
      })
      .catch(error => {
        console.error('Error fetching user details:', error.message);
      });
  }, [id, authToken]);

  if (!bookDetails) {
    return <p>Loading...</p>;
  }

  const handleStarClick = (starId) => {
    setUserRating(starId);
    rateBook(starId, id, setBookDetails);
  };

  return (
    <div className='book-details-container'>
      <div className="book-details-buttons">
        <div className="book-details">
          <div className="book-details-header">
            <h2>{bookDetails.name}</h2>
            <p>{bookDetails.author}</p>
            <p className='description'>{bookDetails.description}</p>
            <p>Price: {bookDetails.price}</p>
            {isUserAuth ? (
              <div><StarRating rating={userRating} onStarClick={handleStarClick}></StarRating></div>
            ) : (
              <div></div>
            )}
            <p>Rating: {bookDetails.average_rating.toFixed(2)} / 5.00</p>
          </div>
          <div className="book-details-content">
            <div className="profile-picture">
              {bookDetails.picture ? (
                <img src={bookDetails.picture} alt={`Book Cover`} />
              ) : (
                <img src="https://nnpdev.wustl.edu/img/bookCovers/genericBookCover.jpg" alt="Book Cover" />
              )}
            </div>
          </div>
        </div>
        {bookDetails.status && (
          <div className='book-buttons'>
            <button className='edit-book-button'>
              <Link to={paths.BookEdit(id)}>Edit</Link>
            </button>
            <button className='delete-book-button'>
              <Link to={paths.BookDelete(id)}>Delete</Link>
            </button>
          </div>
        )}
      </div>
      <div className="book-details-footer">
        <button><Link to={paths.Home}>Back to List</Link></button>
      </div>
    </div>
  );
};
