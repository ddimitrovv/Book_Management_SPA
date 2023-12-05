const baseUrl = 'http://127.0.0.1:8000/'

const urls = {
    Home: baseUrl,
    Login: `${baseUrl}login/`,
    Logout: `${baseUrl}logout/`,
    Register: `${baseUrl}register/`,
    BooksByStatus: (status) => `${baseUrl}books/${status}/`,
    BookDetail: (id) => `/books/${id}`,
  };
  
  export default urls;