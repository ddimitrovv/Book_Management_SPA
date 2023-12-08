import React, { useEffect, useState } from 'react';
import { Link, Route } from 'react-router-dom';
import { useAuth } from './AuthProvider';
import urls from '../appPaths/urls';
import paths from '../appPaths/paths';

export default function Home() {
  const { isAuthenticated } = useAuth();
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      const authToken = localStorage.getItem('authToken');

      const headers = authToken ? {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      } : {'Content-Type': 'application/json',}

      fetch(urls.Home, {
        method: 'GET',
        headers: headers,
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to fetch data');
          }
          return response.json();
        })
        .then(responseData => {
          setData(responseData);
        })
        .catch(error => {
          console.error('Error fetching data:', error.message);
        });
    };
    fetchData();
  }, [isAuthenticated]);

  return (
    <div className='home'>
      <h1>Welcome to Your Library</h1>
        <div className='book-card-wrapper'>
            {data.status && Array.isArray(data.status) ? (
                data.status.map((status, index) => <Card key={index} status={status} />)
            ) : (
                <p>No status data available</p>
            )}
        </div>
    </div>
  );
}


const Card = ({ status }) => {
    const [statusValue, statusLabel] = status;
  
    return (
      <div className="book-card">
        <div className="profile-picture">
          <img
            src="https://img.freepik.com/premium-photo/books-collection-isolated-white-background-vector-illustration-retro-style_941097-2684.jpg"
            alt="Book Cover"
          />
        </div>
        <div className="book-card-wrapper">
          <div className="book-card-info">
            <button className='books-status-button'>
              <Link to={paths.BooksByStatus(statusValue)}>
                <h2>{statusValue}</h2>
              </Link>
            </button>
          </div>
        </div>
      </div>
    );
  };
  