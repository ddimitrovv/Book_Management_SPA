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
            <Route path={paths.BooksByStatus(':status')} element={<BookListByStatus />} />
            <Route path={paths.BookDetail(':id')} element={<BookDetails />} />

          </Routes>
        </AuthProvider>
      </div>

  );
};

export default App;