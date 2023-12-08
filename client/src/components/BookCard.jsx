import React from 'react';
import { Link } from 'react-router-dom';
import paths from '../appPaths/paths';

const BookCard = ({ book }) => {
  const { id, name, author, picture } = book;

  return (
    <div className="book-card">
      <div className="profile-picture">
        {picture ? (
          <img src={picture} alt={`Book Cover - ${name}`} />
        ) : (
          <img src="https://nnpdev.wustl.edu/img/bookCovers/genericBookCover.jpg" alt="Book Cover" />
        )}
      </div>
      <div className="book-card-wrapper">
        <div className="book-card-info">
          <h2 className='book-title'>{name}</h2>
          <p>{author}</p>
          <button><Link to={`${paths.BookDetail(id)}`}>View Details</Link></button>
        </div>
      </div>
    </div>
  );
};

export default BookCard;
