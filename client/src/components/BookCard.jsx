import React from 'react';
import { Link } from 'react-router-dom';
import paths from '../appPaths/paths';

const BookCard = ({ book }) => {
  const { id, name, author, picture, description } = book;

  return (
    <div className="book-card">
      <div className="profile-picture">
        {picture ? (
          <img src={picture} alt={`Book Cover - ${name}`} />
        ) : (
          <img src="https://via.placeholder.com/200" alt="Book Cover" />
        )}
      </div>
      <div className="book-card-wrapper">
        <div className="book-card-info">
          <h2 className='book-title'>{name}</h2>
          <p>{author}</p>
          <p>{description}</p>
          <button><Link to={`${paths.BookDetail(id)}`}>View Details</Link></button>
        </div>
      </div>
    </div>
  );
};

export default BookCard;
