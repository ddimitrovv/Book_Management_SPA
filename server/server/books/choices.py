from django.db import models


class BookStatusChoices(models.TextChoices):
    """
    Choices for the status of a book.

    This class defines predefined choices for the status of a book. Each choice
    consists of a human-readable name and its corresponding database value.

    Choices:
    - READ: The book has been read.
    - IN_PROGRESS: The book is currently being read.
    - UNREAD: The book has not been read.
    - TO_BUY: The user wants to buy this book.
    """

    READ = 'Read', 'Read'
    IN_PROGRESS = 'Reading', ' Reading'
    UNREAD = 'Unread', 'Unread'
    TO_BUY = 'Want to Buy', 'Want to Buy'


class BookGenreChoices(models.TextChoices):
    """
    Choices for the genre of a book.

    This class defines predefined choices for the genre of a book. Each choice
    consists of a human-readable name and its corresponding database value.

    Choices:
    - FICTION: Fictional works.
    - NON_FICTION: Factual and informative works.
    - MYSTERY: Mystery and detective stories.
    - SCIENCE_FICTION: Speculative and futuristic works.
    - FANTASY: Imaginary and fantastical works.
    - ROMANCE: Romantic stories.
    - HORROR: Horror and scary stories.
    - THRILLER: Suspenseful and thrilling stories.
    - HISTORICAL_FICTION: Fiction set in historical periods.
    - BIOGRAPHY: Life stories of real people.
    - AUTOBIOGRAPHY: Author's own life story.
    - SELF_HELP: Self-help and personal development.
    - BUSINESS: Books related to business and entrepreneurship.
    - TRAVEL: Travel and adventure.
    - COOKING: Culinary and cooking books.
    - SCIENCE: Scientific and educational works.
    - PHILOSOPHY: Philosophical and thought-provoking works.
    - POETRY: Poetic and verse works.
    - CHILDRENS: Books for children.
    - YOUNG_ADULT: Books for young adults.
    - COMICS: Graphic novels and comic books.
    """

    NOVEL = 'Novel', 'Novel'
    FICTION = 'Fiction', 'Fiction'
    NON_FICTION = 'Non-Fiction', 'Non-Fiction'
    MYSTERY = 'Mystery', 'Mystery'
    SCIENCE_FICTION = 'Science Fiction', 'Science Fiction'
    FANTASY = 'Fantasy', 'Fantasy'
    ROMANCE = 'Romance', 'Romance'
    HORROR = 'Horror', 'Horror'
    THRILLER = 'Thriller', 'Thriller'
    HISTORICAL_FICTION = 'Historical Fiction', 'Historical Fiction'
    BIOGRAPHY = 'Biography', 'Biography'
    AUTOBIOGRAPHY = 'Autobiography', 'Autobiography'
    SELF_HELP = 'Self-Help', 'Self-Help'
    BUSINESS = 'Business', 'Business'
    TRAVEL = 'Travel', 'Travel'
    COOKING = 'Cooking', 'Cooking'
    SCIENCE = 'Science', 'Science'
    PHILOSOPHY = 'Philosophy', 'Philosophy'
    POETRY = 'Poetry', 'Poetry'
    CHILDREN = 'Children', 'Children'
    YOUNG_ADULT = 'Young Adult', 'Young Adult'
    COMICS = 'Comics', 'Comics'
