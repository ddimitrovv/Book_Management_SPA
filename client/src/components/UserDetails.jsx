import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import paths from '../appPaths/paths';
import urls from '../appPaths/urls';

const UserDetails = () => {
  const authToken = localStorage.getItem('authToken');
  const [userDetails, setUserDetails] = useState();

  useEffect(() => {
    fetch(urls.UserDetails, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      },
    })
      .then(response => response.json())
      .then(data => {
        setUserDetails(data);
      })
      .catch(error => {
        console.error('Error fetching user details:', error.message);
      });
  }, [authToken]);

  if (!userDetails) {
    return <p></p>;
  }

  return (
    <div className='user-details-wrapper'>
        <div className="user-details">
            <div className="profile-picture">
                {userDetails.user_profile.profile_picture ? (
                <img src={userDetails.user_profile.profile_picture} alt={`Profile Picture`} />
                ) : (
                <img src="https://via.placeholder.com/200" alt="Book Cover" />
                )}
            </div>
            <div className="book-card-wrapper">
                <div className="book-card-info">
                <p>First name: <span>{userDetails.user_profile.first_name}</span></p>
                <p>Last name: <span>{userDetails.user_profile.last_name}</span></p>
                <p>Gender: <span>{userDetails.user_profile.gender}</span></p>
                <p>Username: <span>{userDetails.user.username}</span></p>
                <p>Email: <span>{userDetails.user.email}</span></p>
                {/* <button><Link to={`${paths.BookDetail(userDetails.user.id)}`}>View Details</Link></button> */}
                </div>
            </div>
        </div>
    </div>
  );
};

export default UserDetails;
