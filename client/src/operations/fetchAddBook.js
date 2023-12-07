import paths from "../appPaths/paths";
import urls from "../appPaths/urls";

export default function fetchAddBook(name, author, picture, description, bookStatus, price, navigate) {

    const authToken = localStorage.getItem('authToken');
    const headers = authToken
      ? {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        }
      : { 'Content-Type': 'application/json' };

    const body = JSON.stringify({
        name,
        author,
        picture: picture || null,
        description: description || null,
        status: bookStatus,
        price: price || null
    });

    fetch(urls.AddBook, {
      method: 'POST',
      headers: headers,
      body: body
    })
    .then(response => {
      if (response.status !== 201) {
        throw new Error(`${response.status} (${response.statusText})`);
      }
      return response.json();
    })
    .then((data) => {
      navigate(paths.Home)
    })
    .catch(error => {
      console.error('Error adding book:', error.message);
    });
};