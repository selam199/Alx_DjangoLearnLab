# Project Setup and User Authentication for a Social Media API

A complete implementation of custom user model with token-based authentication in Django REST Framework.

## Features

- Custom user model with extended fields (bio, profile picture)
- User following/followers system
- Token-based authentication
- REST API endpoints for registration
- Secure password handling


## API Endpoints

### Authentication

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | Register new user |
| `/api/auth/login/` | POST | Login existing user |

### Posts

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/posts/` | GET | List all posts |
| `/api/posts/` | POST | Create new post |
| `/api/posts/{id}/` | GET | Get specific post |
| `/api/posts/{id}/` | PUT/PATCH | Update post |
| `/api/posts/{id}/` | DELETE | Delete post |
| `/api/posts/user_posts/` | GET | Get current user's posts |

### Comments
Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/posts/{post_id}/comments/` | GET | List all comments for a post |
| `/api/posts/{post_id}/comments/` | POST | Create new comment on post |
| `/api/posts/{post_id}/comments/{id}/` | GET | Get specific comment |
| `/api/posts/{post_id}/comments/{id}/` | PUT/PATCH | Update comment |
| `/api/posts/{post_id}/comments/{id}/` | DELETE | Delete comment |

## Query Parameters

### Pagination
- `page` - Page number
- `page_size` - Items per page (default: 10)

### Filtering
- `author` - Filter posts by author ID
- `search` - Search in title and content
- `ordering` - Sort results (`created_at`, `-created_at`, `title`, etc.)