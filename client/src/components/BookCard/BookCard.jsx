import React from 'react';
import { Link } from 'react-router-dom';
import paths from '../../appPaths/paths';
import styles from './BookCard.module.css'

const BookCard = ({ book }) => {
  const { id, name, author, picture, average_rating } = book ?? {};

  return (
    <Link to={`${paths.BookDetail(id)}`}>
      <div className={styles.bookCard}>
        <div className={styles.bookCardPicture}>
          {picture ? (
            <img src={picture} alt={`Book Cover - ${name}`} />
          ) : (
            <img src="https://nnpdev.wustl.edu/img/bookCovers/genericBookCover.jpg" alt="Book Cover" />
          )}
        </div>
        <div className={styles.bookCardWrapper}>
          <div className={styles.bookCardInfo}>
            <h2 className={styles.bookTitle}>{name}</h2>
            <p>{author}</p>
            <p className={styles.bookRating}>Rating: {average_rating.toFixed(2)} / 5.00</p>
            
          </div>
        </div>
      </div>
    </Link>
  );
};

export default BookCard;
