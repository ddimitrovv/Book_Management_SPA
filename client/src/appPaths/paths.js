const paths = {
    Home: '/',
    Login: '/login',
    Logout: '/logout',
    Register: '/register',
    BooksByStatus: (status) => `/books/${status}`,
    BookDetail: (id) => `/books/${id}`,
    AddBook: '/books/create',
    UserDetails: `/users`,
    EditUser: `/users/edit`,
  };
  
  export default paths;