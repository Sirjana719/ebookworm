# E-BookWorm Project Structure

```
ebookworm/
│
├── app.py                          # Main Flask application
├── models.py                       # Database models
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── database.db                     # SQLite database (auto-created)
├── init_db.py                      # Database initialization script
│
├── routes/                         # Route handlers
│   ├── __init__.py
│   ├── auth.py                     # Authentication routes
│   ├── books.py                    # Book management routes
│   └── cart.py                     # Shopping cart routes
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── index.html                  # Homepage
│   ├── books.html                  # Books listing page
│   ├── book_detail.html            # Single book detail page
│   ├── login.html                  # Login page
│   ├── register.html               # Registration page
│   ├── cart.html                   # Shopping cart page
│   ├── profile.html                # User profile page
│   └── admin/                      # Admin templates
│       ├── dashboard.html          # Admin dashboard
│       ├── add_book.html           # Add new book
│       └── manage_books.html       # Manage books
│
├── static/                         # Static files
│   ├── css/
│   │   └── style.css               # Main stylesheet
│   ├── js/
│   │   └── main.js                 # JavaScript functionality
│   └── images/
│       ├── logo.png                # Site logo
│       └── books/                  # Book cover images
│
├── .gitignore                      # Git ignore file
└── README.md                       # Project documentation
```

## File Descriptions

### Core Files

- **app.py**: Entry point of the Flask application, initializes the app and registers blueprints
- **models.py**: SQLAlchemy models for User, Category, Book, and Cart
- **config.py**: Application configuration (secret key, database URI, etc.)
- **init_db.py**: Script to create tables and populate sample data

### Routes

- **auth.py**: User registration, login, logout functionality
- **books.py**: Display books, search, filter by category, book details
- **cart.py**: Add to cart, remove from cart, view cart

### Templates

All HTML files use Jinja2 templating and extend from base.html

### Static Files

- **style.css**: Contains all styling with modern, clean design
- **main.js**: Client-side interactivity, form validation, AJAX calls
- **images/**: Placeholder for logos and book covers

## Database Schema

### Users Table
- id (Primary Key)
- name
- email (Unique)
- password (Hashed)
- is_admin (Boolean)

### Categories Table
- id (Primary Key)
- category_name

### Books Table
- id (Primary Key)
- title
- author
- price
- description
- category_id (Foreign Key → categories.id)
- image_url
- stock

### Cart Table
- id (Primary Key)
- user_id (Foreign Key → users.id)
- book_id (Foreign Key → books.id)
- quantity

## Key Features

✅ User authentication with session management
✅ Book catalog with categories
✅ Search and filter functionality
✅ Shopping cart
✅ Admin panel for book management
✅ Responsive design
✅ Form validation (client and server-side)
✅ Clean, modern UI
