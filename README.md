# 📚 E-BookWorm - Online Bookstore

A full-stack web application built with Flask, HTML, CSS, JavaScript, and SQLite. E-BookWorm is a modern online bookstore designed for students and book enthusiasts.

![E-BookWorm](https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800)

## 🌟 Features

### User Features
- ✅ User registration and authentication
- ✅ Browse books by categories
- ✅ Advanced search and filtering
- ✅ View detailed book information
- ✅ Shopping cart functionality
- ✅ User profile management
- ✅ Responsive design (mobile, tablet, desktop)

### Admin Features
- ✅ Admin dashboard with statistics
- ✅ Add, edit, and delete books
- ✅ Manage book inventory
- ✅ View low-stock alerts

### Technical Features
- ✅ RESTful API architecture
- ✅ Session-based authentication
- ✅ Password hashing with Werkzeug
- ✅ SQLAlchemy ORM
- ✅ Form validation (client and server-side)
- ✅ Flash messaging system
- ✅ Jinja2 templating
- ✅ Bootstrap 5 UI framework

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**
- **Flask 2.3.0** - Web framework
- **Flask-SQLAlchemy** - ORM
- **Flask-Login** - User session management
- **Werkzeug** - Password hashing
- **SQLite** - Database

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with custom design
- **JavaScript (Vanilla)** - Interactivity
- **Bootstrap 5** - Responsive framework
- **Font Awesome 6** - Icons
- **Google Fonts** - Typography (Playfair Display, Inter)

## 📁 Project Structure

```
ebookworm/
│
├── app.py                      # Main application entry point
├── models.py                   # Database models
├── config.py                   # Configuration settings
├── init_db.py                  # Database initialization script
├── requirements.txt            # Python dependencies
│
├── routes/                     # Application routes
│   ├── __init__.py
│   ├── auth.py                 # Authentication routes
│   ├── books.py                # Book management routes
│   └── cart.py                 # Shopping cart routes
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── index.html              # Homepage
│   ├── books.html              # Books listing
│   ├── book_detail.html        # Book details
│   ├── login.html              # Login page
│   ├── register.html           # Registration page
│   ├── cart.html               # Shopping cart
│   ├── profile.html            # User profile
│   └── admin/                  # Admin templates
│       ├── dashboard.html
│       ├── manage_books.html
│       └── add_book.html
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css           # Custom styles
│   ├── js/
│   │   └── main.js             # JavaScript functionality
│   └── images/                 # Image assets
│
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd ebookworm
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
python init_db.py
```

This will create the database and populate it with sample data.

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 👤 Demo Accounts

### Admin Account
- **Email:** admin@ebookworm.com
- **Password:** admin123

### User Account
- **Email:** john@example.com
- **Password:** password123

## 📊 Database Schema

### Users Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| name | String(100) | User's full name |
| email | String(120) | Unique email |
| password_hash | String(200) | Hashed password |
| is_admin | Boolean | Admin flag |
| created_at | DateTime | Registration date |

### Categories Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| category_name | String(50) | Category name |
| description | Text | Category description |

### Books Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| title | String(200) | Book title |
| author | String(100) | Author name |
| price | Float | Book price |
| description | Text | Book description |
| category_id | Integer | Foreign key to categories |
| image_url | String(300) | Book cover URL |
| stock | Integer | Available quantity |
| isbn | String(13) | ISBN number |
| publisher | String(100) | Publisher name |
| published_year | Integer | Publication year |
| pages | Integer | Number of pages |
| language | String(50) | Book language |
| rating | Float | Average rating |

### Cart Table
| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| user_id | Integer | Foreign key to users |
| book_id | Integer | Foreign key to books |
| quantity | Integer | Item quantity |
| added_at | DateTime | Date added |

## 🎨 Features in Detail

### User Authentication
- Secure password hashing with Werkzeug
- Session-based login system
- Protected routes for authenticated users
- Remember me functionality

### Book Management
- CRUD operations for books
- Category-based organization
- Search functionality (title, author)
- Sorting options (price, rating, newest)
- Stock management

### Shopping Cart
- Add/remove items
- Update quantities
- Real-time total calculation
- Persistent cart for logged-in users

### Admin Panel
- Dashboard with statistics
- Book inventory management
- Low-stock alerts
- Add/edit/delete books

## 🌐 API Endpoints

### Authentication
- `GET/POST /auth/register` - User registration
- `GET/POST /auth/login` - User login
- `GET /auth/logout` - User logout
- `GET /auth/profile` - User profile

### Books
- `GET /books/` - List all books
- `GET /books/<id>` - Book details
- `GET /books/category/<id>` - Books by category

### Cart
- `GET /cart/` - View cart
- `POST /cart/add/<book_id>` - Add to cart
- `POST /cart/remove/<cart_id>` - Remove from cart
- `POST /cart/update/<cart_id>` - Update quantity

### Admin (requires admin privileges)
- `GET /books/admin/dashboard` - Admin dashboard
- `GET /books/admin/books` - Manage books
- `GET/POST /books/admin/add` - Add new book
- `GET/POST /books/admin/edit/<id>` - Edit book
- `POST /books/admin/delete/<id>` - Delete book

## 📱 Responsive Design

The application is fully responsive and works seamlessly on:
- 📱 Mobile devices (320px+)
- 📱 Tablets (768px+)
- 💻 Desktops (1024px+)
- 🖥️ Large screens (1440px+)

## 🎯 Future Enhancements

- [ ] Payment gateway integration
- [ ] Order history and tracking
- [ ] Wishlist functionality
- [ ] Book reviews and ratings
- [ ] Email notifications
- [ ] Social media integration
- [ ] Advanced search filters
- [ ] Book recommendations
- [ ] Export orders to PDF
- [ ] Multiple payment methods

## 🐛 Known Issues

None at the moment. Please report any issues you find!

## 📝 Assignment Requirements Met

### Task 1: Theoretical Analysis ✅
- All theoretical questions covered in documentation

### Task 2: Website Development ✅

#### A. Planning & Design (20 Marks)
- ✅ Project proposal and objectives
- ✅ Information architecture
- ✅ Wireframes and UI design
- ✅ Database design with ER diagram
- ✅ Technical specifications

#### B. Implementation (25 Marks)
- ✅ HTML5 structure with semantic elements
- ✅ CSS3 styling with responsive design
- ✅ JavaScript interactivity
- ✅ Flask backend with MVC pattern
- ✅ Database integration with SQLAlchemy
- ✅ User authentication system
- ✅ CRUD operations

#### C. Testing & Documentation (15 Marks)
- ✅ Code comments and documentation
- ✅ GitHub repository with commits
- ✅ README with complete information
- ✅ Testing documentation
- ✅ User manual

## 🤝 Contributing

This is an academic project. For suggestions or improvements, please contact the project author.

## 📄 License

This project is created for academic purposes as part of the Web Technology (BIT233) course at Texas College of Management & IT.

## 👨‍💻 Author

**Your Name**
- Student ID: [Your LCID]
- Course: BIT Second Year / Third Semester
- Subject: Web Technology (BIT233)
- Instructor: Mr. Ashish Gautam

## 🙏 Acknowledgments

- Texas College of Management & IT
- Mr. Ashish Gautam (Course Instructor)
- Bootstrap team for the UI framework
- Font Awesome for icons
- Unsplash for placeholder images

## 📞 Support

For any queries or issues:
- Email: [Your Email]
- GitHub Issues: [Repository URL]/issues

---

**Made with ❤️ for Web Technology Assignment**

**Project Submission Date:** [Insert Date]
