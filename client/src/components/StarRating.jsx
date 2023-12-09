import React from 'react';

const StarRating = ({ rating }) => {
  const renderStars = () => {
    const stars = [];

    for (let i = 1; i <= 5; i++) {
      const starType = i <= rating ? 'full' : 'empty';
      stars.push(<span key={i} className={`star ${starType}`}>&#9733;</span>);
    }

    return stars;
  };

  return <div className="star-rating">{renderStars()}</div>;
};

export default StarRating;
