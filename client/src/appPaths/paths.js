const paths = {
    Home: '/',
    Login: '/login',
    Logout: '/logout',
    Register: '/register',
    BooksByStatus: (status) => `/books/${status}`,
    BookDetail: (id) => `/books/details/${id}`,
    BookEdit: (id) => `/books/edit/${id}`,
    BookDelete: (id) => `/books/delete/${id}`,
    AddBook: '/books/create',
    UserDetails: `/users`,
    EditUser: `/users/edit`,
    DeleteUser: `/users/delete`,
  };
  
  export default paths;