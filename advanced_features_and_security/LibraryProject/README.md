## Permissions and Groups Setup

1. **Custom Permissions**:
   - `can_view`: Allows a user to view a book.
   - `can_create`: Allows a user to create a new book.
   - `can_edit`: Allows a user to edit an existing book.
   - `can_delete`: Allows a user to delete a book.

2. **Groups**:
   - **Editors**: Can create, edit, and view books.
   - **Viewers**: Can only view books.
   - **Admins**: Can view, create, edit, and delete books.

3. **Permissions in Views**:
   - Views that require specific permissions use the `@permission_required` decorator to enforce access control.
This is my README file


## Security Measures

1. **CSRF Protection**: All forms include `{% csrf_token %}` to protect against CSRF attacks.
2. **SQL Injection Prevention**: All database queries use Django's ORM to ensure proper parameterized queries.
3. **CSP Header**: Configured Content Security Policy headers to mitigate XSS attacks.
4. **Secure Cookies**: CSRF and session cookies are sent only over HTTPS.
5. **Secure Headers**: Enabled secure headers like X-Frame-Options, HSTS, and Content-Type-Nosniff to protect against clickjacking and other vulnerabilities.

Make sure to always use `DEBUG=False` in production environments to avoid exposing sensitive information.
