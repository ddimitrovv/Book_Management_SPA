const baseUrl = 'http://127.0.0.1:8000/api/'

const urls = {
    Home: baseUrl,
    Login: `${baseUrl}login/`,
    Logout: `${baseUrl}logout/`,
    Register: `${baseUrl}register/`,
    MyBooks: `${baseUrl}my-books/`,
    BooksByStatus: (status) => `${baseUrl}books/${status}/`,
    BookDetail: (id) => `${baseUrl}books/details/${id}/`,
    BookEdit: (id) => `${baseUrl}books/edit/${id}/`,
    BookDelete: (id) => `${baseUrl}books/delete/${id}/`,
    RateBook: (id) => `${baseUrl}books/rate-book/${id}/`,
    AddBook: `${baseUrl}books/create/`,
    UserDetails: `${baseUrl}users/`,
    EditUser: `${baseUrl}users/update-profile/`,
    DeleteUser: `${baseUrl}users/delete/`,
  };
  
  export default urls;