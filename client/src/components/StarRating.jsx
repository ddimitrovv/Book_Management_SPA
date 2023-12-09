import React, { useState } from 'react';

const StarRating = ({ rating, onStarClick }) => {
  const [hoveredRating, setHoveredRating] = useState(null);

  const handleStarClick = (star) => {
    onStarClick(star);
  };

  const renderStars = () => {
    const stars = [];

    for (let i = 1; i <= 5; i++) {
      const starType = i <= (hoveredRating || rating) ? 'full' : 'empty';
      stars.push(
        <span
          id={i}
          key={i}
          className={`star ${starType}`}
          onClick={() => handleStarClick(i)}
          onMouseEnter={() => setHoveredRating(i)}
          onMouseLeave={() => setHoveredRating(null)}
        >
          &#9733;
        </span>
      );
    }

    return stars;
  };

  return <div className="star-rating">{renderStars()}</div>;
};

export default StarRating;
