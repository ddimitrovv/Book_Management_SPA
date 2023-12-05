import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './AuthProvider';
import urls from '../appPaths/urls';

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
          console.log('data:');
          console.log(responseData);
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
            src="https://via.placeholder.com/200"
            alt="Book Cover"
          />
        </div>
        <div className="book-card-wrapper">
          <div className="book-card-info">
            <Link to={`${urls.Books}${statusValue}/`}>
              <h2>{statusValue}</h2>
            </Link>
          </div>
        </div>
      </div>
    );
  };
  