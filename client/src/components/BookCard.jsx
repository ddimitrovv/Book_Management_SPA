import React from 'react';
import { Link } from 'react-router-dom';
import paths from '../appPaths/paths';

const BookCard = ({ book }) => {
  const { id, name, author, picture, average_rating } = book ?? {};

  return (
    <Link to={`${paths.BookDetail(id)}`}>
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
            <p className='book-rating'>Rating: {average_rating}</p>
            
          </div>
        </div>
      </div>
    </Link>
  );
};

export default BookCard;
