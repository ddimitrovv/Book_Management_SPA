import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import paths from '../../appPaths/paths';
import urls from '../../appPaths/urls';
import styles from './UserDetails.module.css';

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
    <div className={styles.userDetailsWrapper}>
        <div className={styles.userDetails}>
            <div className={styles.profilePicture}>
                {userDetails.user_profile.profile_picture ? (
                <img src={userDetails.user_profile.profile_picture} alt={`Profile Picture`} />
                ) : (
                <img src="https://as2.ftcdn.net/v2/jpg/00/64/67/63/1000_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg" alt="Book Cover" />
                )}
            </div>
            <div className={styles.userCardInfo}>
                <p>First name: <span>{userDetails.user_profile.first_name}</span></p>
                <p>Last name: <span>{userDetails.user_profile.last_name}</span></p>
                <p>Gender: <span>{userDetails.user_profile.gender}</span></p>
                <p>Username: <span>{userDetails.user.username}</span></p>
                <p>Email: <span>{userDetails.user.email}</span></p>
            </div>
            <div className={styles.userDetailsButtons}>
                <button className={styles.editUserButton}>
                    <Link to={{ pathname: paths.EditUser, state: { userDetails } }}>Edit</Link>
                </button>
                <button className={styles.deleteUserButton}>
                    <Link to={paths.DeleteUser}>Delete</Link>
                </button>
            </div>

        </div>
    </div>
  );
};

export default UserDetails;
