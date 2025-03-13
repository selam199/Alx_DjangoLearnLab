# Advanced API Project

This project demonstrates how to use Django REST Framework's generic views and custom serializers.

## API Endpoints

### Retrieve all books
- `GET /api/books/`
- **Response**: List of all books.

### Retrieve a single book
- `GET /api/books/<id>/`
- **Response**: Details of a specific book.

### Create a new book (Authenticated users only)
- `POST /api/books/`
- **Body**: `{ "title": "Book Title", "publication_year": 2024, "author": 1 }`

### Update a book (Authenticated users only)
- `PUT /api/books/<id>/`

### Delete a book (Authenticated users only)
- `DELETE /api/books/<id>/`
# Advanced API Project - Book CRUD Operations

## Endpoints
- **GET /books/** - Retrieve a list of all books.
- **GET /books/<int:pk>/** - Retrieve a single book by its ID.
- **POST /books/create/** - Create a new book (Authenticated users only).
- **PUT /books/<int:pk>/update/** - Update an existing book (Authenticated users only).
- **DELETE /books/<int:pk>/delete/** - Delete a book (Authenticated users only).

## Permissions
- `IsAuthenticatedOrReadOnly` - Allows unauthenticated users to view books but restricts modification.
- `IsAuthenticated` - Requires authentication for modifying or deleting books.
- `IsOwnerOrReadOnly` - Ensures only the owner of the book can modify or delete it.
