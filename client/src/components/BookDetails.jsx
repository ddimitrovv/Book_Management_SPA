import React from 'react';
import { Link } from 'react-router-dom';
import paths from '../appPaths/paths';

const BookDetails = ({ book }) => {
  const { id, name, author, picture, description } = book;

  return (
    <div className="book-details">
      <div className="book-details-header">
        <h2>{name}</h2>
        <p>{author}</p>
      </div>
      <div className="book-details-content">
        <div className="profile-picture">
          {picture ? (
            <img src={picture} alt={`Book Cover - ${name}`} />
          ) : (
            <img src="https://via.placeholder.com/200" alt="Book Cover" />
          )}
        </div>
        <div className="book-description">
          <p>{description}</p>
        </div>
      </div>
      <div className="book-details-footer">
        <button><Link to={`${paths.BookList}`}>Back to List</Link></button>
      </div>
    </div>
  );
};

export default BookDetails;
