API Authentication and Permissions
Authentication Method:

The API uses Token-based Authentication. To authenticate, users must obtain an authentication token and include it in the Authorization header for requests that require authentication.
The token is retrieved by sending a POST request with the user’s username and password to the /api-token-auth/ endpoint.
Permissions:

IsAuthenticated: All views in the API are protected by the IsAuthenticated permission, meaning only logged-in users can access any data.
IsAdminUser: Certain actions (e.g., creating, updating, or deleting books) are restricted to users who have admin privileges. This permission is applied via IsAdminUser.
Custom Permissions:
IsAuthor: In certain views, such as the BookViewSet, the custom IsAuthor permission ensures that only the user who created a book (the author) can modify or delete it.