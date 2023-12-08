import React, { useState } from 'react';
import fetchAddBook from '../operations/fetchAddBook';
import { useNavigate } from 'react-router-dom';
// import { useAuth } from './AuthProvider';


const AddBook = () => {
//   const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [author, setAuthor] = useState('');
  const [picture, setPicture] = useState('');
  const [description, setDescription] = useState('');
  const [bookStatus, setBookStatus] = useState('Read');
  const [price, setPrice] = useState('');

  const handleAddBook = async () => {
    fetchAddBook(name, author, picture, description, bookStatus, price, navigate)
  };

  return (
    <div className='add-book-form'>
      <div className='form'>
        <h2>Add Book</h2>
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
            value={description} 
            onChange={(e) => setDescription(e.target.value)} />
        </div>
        <div>
            <label>Choose a book status:</label>
            <select 
              value={bookStatus} 
              onChange={(e) => setBookStatus(e.target.value)}
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
        <button onClick={handleAddBook}>Add Book</button>
      </div>
    </div>
  );
};

export default AddBook;
