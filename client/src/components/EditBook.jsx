import React, { useState, useEffect } from 'react';
import urls from '../appPaths/urls';
import paths from '../appPaths/paths';
import { useNavigate, useParams } from 'react-router-dom';

const EditBook = () => {

  const navigate = useNavigate();

  const authToken = localStorage.getItem('authToken');

  const { id } = useParams();

  const [name, setName] = useState('');
  const [author, setAuthor] = useState('');
  const [picture, setPicture] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('');
  const [price, setPrice] = useState('');

  useEffect(() => {
    fetch(urls.BookDetail(id), {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      },
    })
      .then(response => response.json())
      .then(data => {
        setName(data.book.name);
        setAuthor(data.book.author);
        setPicture(data.book.picture || '');
        setDescription(data.book.description || '');
        setStatus(data.book.status);
        setPrice(data.book.price || '');
      })
      .catch(error => {
        console.error('Error fetching user details:', error.message);
      });
  }, [authToken]);

  // Function to handle form submission
  const handleEditBook = (event) => {
    event?.preventDefault();
  
    const bookData = {
      name: name,
      author: author,
      picture: picture || null,
      description: description || null,
      status: status,
      price: price || null,
    };
  
    fetch(urls.BookEdit(id), {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${authToken}`,
      },
      body: JSON.stringify(bookData),
    })
      .then(response => {
        if (!response.ok) {
          // Handle error response
          throw new Error('Failed to update book');
        }
        // Handle success, e.g., show a success message
        navigate(paths.BookDetail(id));

      })
      .catch(error => {
        console.error('Error updating book:', error.message);
        // Handle error, e.g., show an error message to the user
      });
  };
  

  return (
    <div className='add-book-form'>
      <div className='form'>
        <h2>Edit Book</h2>
        <div>
          <label>Title:</label>
          <input 
            type="text" 
            autoComplete='on' 
            placeholder='Enter book title' 
            value={name} 
            onChange={(e) => setName(e.target.value)} />
        </div>
        <div>
          <label>Author:</label>
          <input 
            type="text" 
            placeholder='Enter author name' 
            value={author} 
            onChange={(e) => setAuthor(e.target.value)} />
        </div>
        <div>
          <label>Picture:</label>
          <input 
            type="url" 
            placeholder='Enter image url' 
            value={picture} 
            onChange={(e) => setPicture(e.target.value)} />
        </div>
        <div>
          <label>Description:</label>
          <textarea 
            rows="7" 
            cols="23" 
            placeholder='Enter book description' 
            value={description || ''} 
            onChange={(e) => setDescription(e.target.value)} />
        </div>
        <div>
            <label>Choose a book status:</label>
            <select 
              value={status} 
              onChange={(e) => setStatus(e.target.value)}
              >
                <option value="Read">Read</option>
                <option value="Reading">Reading</option>
                <option value="Unread">Unread</option>
                <option value="Want to Buy">Want to Buy</option>
            </select>
        </div>
        <div>
            <label>Book Price:</label>
            <input 
              type="number" 
              min="0.00" 
              max="10000.00" 
              step="0.01" 
              placeholder='0.00' 
              value={price} 
              onChange={(e) => setPrice(e.target.value)} />
        </div>
        <button onClick={handleEditBook}>Edit Book</button>
      </div>
    </div>
  );
};

export default EditBook;
