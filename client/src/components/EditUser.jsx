import React, { useState, useEffect } from 'react';
import urls from '../appPaths/urls';

const EditUser = ({ location }) => {
    const userDetails = location.state.userDetails || {
      user: {},
      user_profile: {},
    };

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    // TODO: Add logic to handle form submission here
  };

  return (
    <div className='edit-user-form'>
      <h2>Edit User</h2>
      <form className='form' onSubmit={handleSubmit}>
        <div>
            <label>First Name:</label>
            <input
            type="text"
            name="first_name"
            value={userDetails.user_profile.first_name || ''}
            // TODO:  Add onChange handler if you want to allow editing
          />
        </div>
        <div>
            <label>Last Name:</label>
            <input
            type="text"
            name="last_name"
            value={userDetails.user_profile.last_name || ''}
            // TODO:  Add onChange handler if you want to allow editing
          />
        </div>
        <div>
            <label>Username:</label>
            <input
            type="text"
            name="username"
            value={userDetails.user_profile.username || ''}
            // TODO:  Add onChange handler if you want to allow editing
          />
        </div>
        <div>
            <label>Email:</label>
            <input
            type="text"
            name="email"
            value={userDetails.user_profile.email || ''}
            // TODO:  Add onChange handler if you want to allow editing
          />
        </div>
        <button>Save Changes</button>
      </form>
    </div>
  );
};

export default EditUser;
