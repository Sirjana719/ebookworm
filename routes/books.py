"""
Book management routes - browsing, searching, and viewing books
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import db, Book, Category
from sqlalchemy import or_

books_bp = Blueprint('books', __name__)

@books_bp.route('/')
def all_books():
    """Display all books with filtering and search"""
    # Get query parameters
    search_query = request.args.get('search', '')
    category_id = request.args.get('category', '')
    sort_by = request.args.get('sort', 'newest')
    
    # Base query
    query = Book.query
    
    # Apply search filter
    if search_query:
        query = query.filter(
            or_(
                Book.title.ilike(f'%{search_query}%'),
                Book.author.ilike(f'%{search_query}%'),
                Book.description.ilike(f'%{search_query}%')
            )
        )
    
    # Apply category filter
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Apply sorting
    if sort_by == 'newest':
        query = query.order_by(Book.created_at.desc())
    elif sort_by == 'price_low':
        query = query.order_by(Book.price.asc())
    elif sort_by == 'price_high':
        query = query.order_by(Book.price.desc())
    elif sort_by == 'rating':
        query = query.order_by(Book.rating.desc())
    elif sort_by == 'title':
        query = query.order_by(Book.title.asc())
    
    # Execute query
    books = query.all()
    
    # Get all categories for filter dropdown
    categories = Category.query.all()
    
    return render_template('books.html', 
                         books=books, 
                         categories=categories,
                         search_query=search_query,
                         selected_category=category_id,
                         sort_by=sort_by)


@books_bp.route('/<int:book_id>')
def book_detail(book_id):
    """Display single book details"""
    book = Book.query.get_or_404(book_id)
    
    # Get related books from same category
    related_books = Book.query.filter(
        Book.category_id == book.category_id,
        Book.id != book.id
    ).limit(4).all()
    
    return render_template('book_detail.html', book=book, related_books=related_books)


@books_bp.route('/category/<int:category_id>')
def books_by_category(category_id):
    """Display books filtered by category"""
    category = Category.query.get_or_404(category_id)
    books = Book.query.filter_by(category_id=category_id).all()
    categories = Category.query.all()
    
    return render_template('books.html', 
                         books=books, 
                         categories=categories,
                         selected_category=str(category_id),
                         category_name=category.category_name)


# Admin routes
@books_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Admin dashboard"""
    if not current_user.is_admin:
        flash('Access denied! Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    # Get statistics
    total_books = Book.query.count()
    total_categories = Category.query.count()
    low_stock_books = Book.query.filter(Book.stock < 5).count()
    
    # Get recent books
    recent_books = Book.query.order_by(Book.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_books=total_books,
                         total_categories=total_categories,
                         low_stock_books=low_stock_books,
                         recent_books=recent_books)


@books_bp.route('/admin/books')
@login_required
def manage_books():
    """Manage all books (admin only)"""
    if not current_user.is_admin:
        flash('Access denied! Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    books = Book.query.order_by(Book.created_at.desc()).all()
    return render_template('admin/manage_books.html', books=books)


@books_bp.route('/admin/add', methods=['GET', 'POST'])
@login_required
def add_book():
    """Add new book (admin only)"""
    if not current_user.is_admin:
        flash('Access denied! Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        price = request.form.get('price')
        description = request.form.get('description')
        category_id = request.form.get('category_id')
        stock = request.form.get('stock', 10)
        isbn = request.form.get('isbn')
        publisher = request.form.get('publisher')
        published_year = request.form.get('published_year')
        pages = request.form.get('pages')
        image_url = request.form.get('image_url', 'default.jpg')
        
        # Validation
        if not all([title, author, price, category_id]):
            flash('Please fill all required fields!', 'danger')
            return redirect(url_for('books.add_book'))
        
        try:
            new_book = Book(
                title=title,
                author=author,
                price=float(price),
                description=description,
                category_id=int(category_id),
                stock=int(stock),
                isbn=isbn,
                publisher=publisher,
                published_year=int(published_year) if published_year else None,
                pages=int(pages) if pages else None,
                image_url=image_url
            )
            
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('books.manage_books'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding book: {str(e)}', 'danger')
            return redirect(url_for('books.add_book'))
    
    categories = Category.query.all()
    return render_template('admin/add_book.html', categories=categories)


@books_bp.route('/admin/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    """Edit existing book (admin only)"""
    if not current_user.is_admin:
        flash('Access denied! Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    book = Book.query.get_or_404(book_id)
    
    if request.method == 'POST':
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.price = float(request.form.get('price'))
        book.description = request.form.get('description')
        book.category_id = int(request.form.get('category_id'))
        book.stock = int(request.form.get('stock', 10))
        book.isbn = request.form.get('isbn')
        book.publisher = request.form.get('publisher')
        
        year = request.form.get('published_year')
        book.published_year = int(year) if year else None
        
        page_count = request.form.get('pages')
        book.pages = int(page_count) if page_count else None
        
        image = request.form.get('image_url')
        if image:
            book.image_url = image
        
        try:
            db.session.commit()
            flash('Book updated successfully!', 'success')
            return redirect(url_for('books.manage_books'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating book: {str(e)}', 'danger')
    
    categories = Category.query.all()
    return render_template('admin/add_book.html', book=book, categories=categories, edit_mode=True)


@books_bp.route('/admin/delete/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    """Delete book (admin only)"""
    if not current_user.is_admin:
        flash('Access denied! Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    book = Book.query.get_or_404(book_id)
    
    try:
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting book: {str(e)}', 'danger')
    
    return redirect(url_for('books.manage_books'))
