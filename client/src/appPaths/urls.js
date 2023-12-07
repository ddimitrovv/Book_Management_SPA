const baseUrl = 'http://127.0.0.1:8000/'

const urls = {
    Home: baseUrl,
    Login: `${baseUrl}login/`,
    Logout: `${baseUrl}logout/`,
    Register: `${baseUrl}register/`,
    BooksByStatus: (status) => `${baseUrl}books/${status}/`,
    BookDetail: (id) => `${baseUrl}books/${id}`,
    AddBook: `${baseUrl}books/create/`,
    UserDetails: `${baseUrl}/users/`,
    EditUser: `${baseUrl}/users/update-profile/`,
  };
  
  export default urls;