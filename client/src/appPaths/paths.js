const paths = {
    Home: '/',
    Login: '/login',
    Logout: '/logout',
    Register: '/register',
    MyBooks: '/my-books',
    BooksByStatus: (status) => `/books/${status}`,
    BookDetail: (id) => `/books/details/${id}`,
    BookEdit: (id) => `/books/edit/${id}`,
    BookDelete: (id) => `/books/delete/${id}`,
    RateBook: (id) => `/books/rate-book/${id}`,
    AddBook: '/books/create',
    UserDetails: `/users`,
    EditUser: `/users/edit`,
    DeleteUser: `/users/delete`,
  };
  
  export default paths;