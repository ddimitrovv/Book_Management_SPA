import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './components/Login';
import Navigation from './components/Navigation';
import Logout from './components/Logout';
import { AuthProvider } from './components/AuthProvider';
import paths from './appPaths/paths'; 
import Home from './components/Home';
import BookListByStatus from './components/BookListByStatus';
import BookDetails from './components/BookDetails';
import Register from './components/Register';
import UserDetails from './components/UserDetails';
import EditUser from './components/EditUser';
import AddBook from './components/AddBook';
import EditBook from './components/EditBook'
import BookDelete from './components/BookDelete';
import UserDelete from './components/UserDelete';
import MyBooks from './components/MyBooks';

const App = () => {
  return (

      <div>
        <AuthProvider>
          <Navigation />
          <Routes>

            <Route path={paths.Home} element={<Home />} />
            <Route path={paths.Register} element={<Register />} />
            <Route path={paths.Login} element={<Login />} />
            <Route path={paths.Logout} element={<Logout />} />
            <Route path={paths.MyBooks} element={<MyBooks />} />
            <Route path={paths.BooksByStatus(':status')} element={<BookListByStatus />} />
            <Route path={paths.BookDetail(':id')} element={<BookDetails />} />
            <Route path={paths.BookEdit(':id')} element={<EditBook />} />
            <Route path={paths.BookDelete(':id')} element={<BookDelete />} />
            <Route path={paths.AddBook} element={<AddBook />} />
            <Route path={paths.UserDetails} element={<UserDetails />} />
            <Route path={paths.EditUser} element={<EditUser />} />
            <Route path={paths.DeleteUser} element={<UserDelete />} />

          </Routes>
        </AuthProvider>
      </div>

  );
};

export default App;