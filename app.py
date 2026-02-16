"""
Main Flask application for E-BookWorm
"""
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from models import db, User
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))

# Register blueprints
from routes.auth import auth_bp
from routes.books import books_bp
from routes.cart import cart_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(cart_bp, url_prefix='/cart')

# Home route
@app.route('/')
def index():
    """Homepage route"""
    from models import Book, Category
    
    # Get featured books (latest 6)
    featured_books = Book.query.order_by(Book.created_at.desc()).limit(6).all()
    
    # Get all categories
    categories = Category.query.all()
    
    # Get top-rated books
    top_books = Book.query.order_by(Book.rating.desc()).limit(4).all()
    
    return render_template('index.html', 
                         featured_books=featured_books,
                         categories=categories,
                         top_books=top_books)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('500.html'), 500

# Context processor for cart count
@app.context_processor
def inject_cart_count():
    """Make cart count available to all templates"""
    from flask_login import current_user
    from models import Cart
    
    cart_count = 0
    if current_user.is_authenticated:
        cart_count = Cart.query.filter_by(user_id=current_user.id).count()
    
    return dict(cart_count=cart_count)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
