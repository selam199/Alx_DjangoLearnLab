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
