import urls from "../appPaths/urls";

export default function rateBook(rating, book_id, bookState) {

    const authToken = localStorage.getItem('authToken');
    const headers = authToken
      ? {
          'Content-Type': 'application/json',
          Authorization: `Token ${authToken}`,
        }
      : { 'Content-Type': 'application/json' };

    const body = JSON.stringify({
        rating,
    });

    fetch(urls.RateBook(book_id), {
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
        bookState(data);
    })
    .catch(error => {
      console.error('Error rating book:', error.message);
    });
};