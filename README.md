# Bookshelf-Django

This is a sample Django Web Framework project idea from [this YouTube Video](https://www.youtube.com/watch?v=hbx39adciac).

This is a simple web application built with Django for managing a book library. Users can view a list of books, search for books, view details of individual books, and browse books by categories.

## Features

- View a list of books available in the library.
- Search for books by title.
- View details of individual books including description and cover image.
- Browse books by categories.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your_username/bookshelf-django.git
    ```

2. Navigate to the project directory:

    ```
    cd bookshelf-django
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```
    python manage.py migrate
    ```

5. Run the development server:

    ```
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000` in your web browser.

## Usage

- Navigate to the home page to view a list of books and browse books by categories.
- Use the search bar in the navigation to search for books by title.
- Click on a book title to view detailed information about the book.
- Access the admin interface at `http://localhost:8000/admin` using the default credentials: admin/admin.
