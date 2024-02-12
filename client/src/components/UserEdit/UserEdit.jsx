import React, { useState, useEffect } from 'react';
import urls from '../../appPaths/urls';
import paths from '../../appPaths/paths';
import { useNavigate } from 'react-router-dom';
import styles from './UserEdit.module.css';

const EditUser = () => {

  const navigate = useNavigate();

  const authToken = localStorage.getItem('authToken');

  const [profilePicture, setProfilePicture] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [gender, setGender] = useState('');

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
        const { user, user_profile } = data;
        setProfilePicture(user_profile.profilePicture)
        setFirstName(user_profile.first_name);
        setLastName(user_profile.last_name);
        setEmail(user.email);
        setUsername(user.username);
        setGender(user_profile.gender);
      })
      .catch(error => {
        console.error('Error fetching user details:', error.message);
      });
  }, [authToken]);

  // Function to handle form submission
  const handleSubmit = (event) => {
    event?.preventDefault();
  
    const userData = {
      profile_picture: profilePicture || null,
      first_name: firstName || null,
      last_name: lastName || null,
      email: email || null,
      gender: gender || null,
    };
  
    fetch(urls.EditUser, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      },
      body: JSON.stringify(userData),
    })
      .then(response => {
        if (!response.ok) {
          // Handle error response
          throw new Error('Failed to update user details');
        }
        // Handle success, e.g., show a success message
        navigate(paths.UserDetails);

      })
      .catch(error => {
        console.error('Error updating user details:', error.message);
        // Handle error, e.g., show an error message to the user
      });
  };
  

  return (
    <div className={styles['user-details-wrapper','edit-user-form']}>
        <div className={styles['user-details']}>
            <div className={styles['profile-picture']}>
                {profilePicture ? (
                <img src={profilePicture} alt={`Profile Picture`} />
                ) : (
                <img src="https://as2.ftcdn.net/v2/jpg/00/64/67/63/1000_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg" alt="Book Cover" />
                )}
            </div>
            <div className={styles['edit-user']}>
                <div className={styles.form}>
                <div>
                  <label>Profile Picture:</label>
                  <input
                  type="url"
                  name="profile_picture"
                  value={profilePicture}
                  onChange={(e) => setProfilePicture(e.target.value)}
                />
                </div><div>
                  <label>First Name:</label>
                  <input
                  type="text"
                  name="first_name"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                />
                </div>
                <div>
                  <label>Last Name:</label>
                  <input
                  type="text"
                  name="last_name"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  />
                </div>
                <div>
                  <label htmlFor='username'>Username:</label>
                  <input
                    type="text"
                    name="username"
                    value={username}
                    disabled={true}
                  />
                </div>
                <div>
                  <label>Gender:</label>
                  <select 
                    value={gender} 
                    onChange={(e) => setGender(e.target.value)}
                    >
                    <option value="Female">Female</option>
                    <option value="Male">Male</option>
                    <option value="Other">Other</option>
                  </select>
                </div>
                <div>
                  <label>Email:</label>
                  <input
                  type="text"
                  name="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  />
                </div>
                </div>
            </div>
            <div className={styles['edit-user-buttons']}>
                <button onClick={handleSubmit}>
                    Save Changes
                </button>
            </div>

        </div>
    </div>
  );
};

export default EditUser;
