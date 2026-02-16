"""
Shopping cart routes - add, remove, view cart
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models import db, Cart, Book

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/')
@login_required
def view_cart():
    """Display user's shopping cart"""
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    
    # Calculate total
    total = sum(item.get_subtotal() for item in cart_items)
    
    return render_template('cart.html', cart_items=cart_items, total=total)


@cart_bp.route('/add/<int:book_id>', methods=['POST'])
@login_required
def add_to_cart(book_id):
    """Add book to cart"""
    book = Book.query.get_or_404(book_id)
    
    # Check if book is already in cart
    cart_item = Cart.query.filter_by(
        user_id=current_user.id,
        book_id=book_id
    ).first()
    
    if cart_item:
        # Increment quantity
        cart_item.quantity += 1
        flash(f'Increased quantity of "{book.title}" in cart!', 'success')
    else:
        # Add new item to cart
        new_cart_item = Cart(
            user_id=current_user.id,
            book_id=book_id,
            quantity=1
        )
        db.session.add(new_cart_item)
        flash(f'"{book.title}" added to cart!', 'success')
    
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash('Error adding to cart. Please try again.', 'danger')
    
    # Return JSON for AJAX requests
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart_count = Cart.query.filter_by(user_id=current_user.id).count()
        return jsonify({'success': True, 'cart_count': cart_count})
    
    return redirect(request.referrer or url_for('index'))


@cart_bp.route('/update/<int:cart_id>', methods=['POST'])
@login_required
def update_quantity(cart_id):
    """Update cart item quantity"""
    cart_item = Cart.query.get_or_404(cart_id)
    
    # Verify ownership
    if cart_item.user_id != current_user.id:
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('cart.view_cart'))
    
    quantity = request.form.get('quantity', type=int)
    
    if quantity and quantity > 0:
        cart_item.quantity = quantity
        try:
            db.session.commit()
            flash('Cart updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error updating cart. Please try again.', 'danger')
    else:
        flash('Invalid quantity!', 'danger')
    
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/remove/<int:cart_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    """Remove item from cart"""
    cart_item = Cart.query.get_or_404(cart_id)
    
    # Verify ownership
    if cart_item.user_id != current_user.id:
        flash('Unauthorized action!', 'danger')
        return redirect(url_for('cart.view_cart'))
    
    book_title = cart_item.book.title
    
    try:
        db.session.delete(cart_item)
        db.session.commit()
        flash(f'"{book_title}" removed from cart!', 'info')
    except Exception as e:
        db.session.rollback()
        flash('Error removing item from cart. Please try again.', 'danger')
    
    # Return JSON for AJAX requests
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        cart_count = Cart.query.filter_by(user_id=current_user.id).count()
        return jsonify({'success': True, 'cart_count': cart_count})
    
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/clear', methods=['POST'])
@login_required
def clear_cart():
    """Clear all items from cart"""
    try:
        Cart.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        flash('Cart cleared successfully!', 'info')
    except Exception as e:
        db.session.rollback()
        flash('Error clearing cart. Please try again.', 'danger')
    
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Checkout process"""
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('books.all_books'))
    
    if request.method == 'POST':
        # In a real application, this would process payment
        # For now, we'll just clear the cart
        try:
            Cart.query.filter_by(user_id=current_user.id).delete()
            db.session.commit()
            flash('Order placed successfully! Thank you for your purchase.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error processing order. Please try again.', 'danger')
    
    total = sum(item.get_subtotal() for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)
