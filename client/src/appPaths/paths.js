const paths = {
    Home: '/',
    Login: '/login',
    Logout: '/logout',
    Register: '/register',
    BooksByStatus: (status) => `/books/${status}`,
    BookDetail: (id) => `/books/${id}`,
    UserDetails: `/users`,
  };
  
  export default paths;