import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Login from './components/Login';
import Navigation from './components/Navigation/Navigation';
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
import PrivateRoute from './components/PrivateRoute';
import Footer from './components/Footer/Footer';

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
            <Route path={paths.BookDetail(':id')} element={<PrivateRoute element={<BookDetails />} />} />
            <Route path={paths.MyBooks}  element={<PrivateRoute element={<MyBooks />} />} />
            <Route path={paths.BooksByStatus(':status')} element={<PrivateRoute element={<BookListByStatus />} />} />
            <Route path={paths.BookEdit(':id')} element={<PrivateRoute element={<EditBook />} />} />
            <Route path={paths.BookDelete(':id')} element={<PrivateRoute element={<BookDelete />} />} />
            <Route path={paths.AddBook} element={<PrivateRoute element={<AddBook />} />} />
            <Route path={paths.UserDetails} element={<PrivateRoute element={<UserDetails />} />} />
            <Route path={paths.EditUser} element={<PrivateRoute element={<EditUser />} />} />
            <Route path={paths.DeleteUser} element={<PrivateRoute element={<UserDelete />} />} />
          </Routes>
        <Footer />
      </AuthProvider>
    </div>
  );
};

export default App;