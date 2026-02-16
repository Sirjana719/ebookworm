"""
Database initialization script with sample data
"""
from app import app
from models import db, User, Category, Book

def init_database():
    """Initialize database with sample data"""
    with app.app_context():
        # Create all tables
        db.drop_all()
        db.create_all()
        
        print("📚 Initializing E-BookWorm Database...")
        
        # Create admin user
        admin = User(name='Admin', email='admin@ebookworm.com', is_admin=True)
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Create regular user
        user = User(name='John Doe', email='john@example.com', is_admin=False)
        user.set_password('password123')
        db.session.add(user)
        
        print("✅ Users created")
        
        # Create categories
        categories_data = [
            {'name': 'Programming & Technology', 'desc': 'Books on programming, software development, and technology'},
            {'name': 'Academic & Textbooks', 'desc': 'Academic textbooks and reference materials'},
            {'name': 'Fiction', 'desc': 'Novels and fictional stories'},
            {'name': 'Non-Fiction', 'desc': 'Biographies, history, and factual books'},
            {'name': 'Self-Help', 'desc': 'Personal development and self-improvement'},
            {'name': 'Competitive Exams', 'desc': 'Exam preparation and study guides'},
            {'name': 'Children\'s Books', 'desc': 'Books for children and young readers'},
            {'name': 'Business & Finance', 'desc': 'Business, economics, and finance books'}
        ]
        
        categories = []
        for cat_data in categories_data:
            category = Category(category_name=cat_data['name'], description=cat_data['desc'])
            db.session.add(category)
            categories.append(category)
        
        db.session.commit()
        print("✅ Categories created")
        
        # Create sample books
        books_data = [
            # Programming & Technology
            {
                'title': 'Python Crash Course',
                'author': 'Eric Matthes',
                'price': 899.00,
                'description': 'A hands-on, project-based introduction to programming in Python. Perfect for beginners who want to learn Python quickly.',
                'category': 0,
                'isbn': '9781593279288',
                'publisher': 'No Starch Press',
                'year': 2019,
                'pages': 544,
                'rating': 4.7,
                'stock': 15,
                'image': 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=400'
            },
            {
                'title': 'Clean Code',
                'author': 'Robert C. Martin',
                'price': 1299.00,
                'description': 'A handbook of agile software craftsmanship. Learn how to write clean, maintainable code that stands the test of time.',
                'category': 0,
                'isbn': '9780132350884',
                'publisher': 'Prentice Hall',
                'year': 2008,
                'pages': 464,
                'rating': 4.8,
                'stock': 20,
                'image': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=400'
            },
            {
                'title': 'JavaScript: The Good Parts',
                'author': 'Douglas Crockford',
                'price': 699.00,
                'description': 'A guide to the elegant parts of JavaScript. Learn to use JavaScript effectively and avoid common pitfalls.',
                'category': 0,
                'isbn': '9780596517748',
                'publisher': 'O\'Reilly Media',
                'year': 2008,
                'pages': 176,
                'rating': 4.5,
                'stock': 12,
                'image': 'https://images.unsplash.com/photo-1587620962725-abab7fe55159?w=400'
            },
            {
                'title': 'The Pragmatic Programmer',
                'author': 'Andrew Hunt',
                'price': 1199.00,
                'description': 'Your journey to mastery. A modern classic for software developers looking to improve their craft.',
                'category': 0,
                'isbn': '9780135957059',
                'publisher': 'Addison-Wesley',
                'year': 2019,
                'pages': 352,
                'rating': 4.9,
                'stock': 18,
                'image': 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400'
            },
            
            # Academic & Textbooks
            {
                'title': 'Introduction to Algorithms',
                'author': 'Thomas H. Cormen',
                'price': 1899.00,
                'description': 'The definitive textbook on algorithms. Comprehensive coverage of all major algorithms and data structures.',
                'category': 1,
                'isbn': '9780262033848',
                'publisher': 'MIT Press',
                'year': 2009,
                'pages': 1312,
                'rating': 4.6,
                'stock': 10,
                'image': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400'
            },
            {
                'title': 'Calculus: Early Transcendentals',
                'author': 'James Stewart',
                'price': 1599.00,
                'description': 'The most successful calculus book of its generation. Clear explanations and comprehensive examples.',
                'category': 1,
                'isbn': '9781285741550',
                'publisher': 'Cengage Learning',
                'year': 2015,
                'pages': 1368,
                'rating': 4.4,
                'stock': 8,
                'image': 'https://images.unsplash.com/photo-1509228468518-180dd4864904?w=400'
            },
            {
                'title': 'Principles of Economics',
                'author': 'N. Gregory Mankiw',
                'price': 1399.00,
                'description': 'Learn economics through real-world examples and applications. Perfect for undergraduate students.',
                'category': 1,
                'isbn': '9781305585126',
                'publisher': 'Cengage Learning',
                'year': 2017,
                'pages': 888,
                'rating': 4.3,
                'stock': 14,
                'image': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=400'
            },
            
            # Fiction
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'price': 299.00,
                'description': 'A timeless classic of American literature. The story of Jay Gatsby and his impossible love.',
                'category': 2,
                'isbn': '9780743273565',
                'publisher': 'Scribner',
                'year': 2004,
                'pages': 180,
                'rating': 4.5,
                'stock': 25,
                'image': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400'
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'price': 349.00,
                'description': 'A dystopian masterpiece that remains more relevant than ever. Big Brother is watching.',
                'category': 2,
                'isbn': '9780451524935',
                'publisher': 'Signet Classic',
                'year': 1961,
                'pages': 328,
                'rating': 4.8,
                'stock': 30,
                'image': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400'
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'price': 399.00,
                'description': 'A gripping tale of racial injustice and childhood innocence in the American South.',
                'category': 2,
                'isbn': '9780061120084',
                'publisher': 'Harper Perennial',
                'year': 2006,
                'pages': 324,
                'rating': 4.9,
                'stock': 22,
                'image': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400'
            },
            
            # Self-Help
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'price': 599.00,
                'description': 'Tiny changes, remarkable results. An easy and proven way to build good habits and break bad ones.',
                'category': 4,
                'isbn': '9780735211292',
                'publisher': 'Avery',
                'year': 2018,
                'pages': 320,
                'rating': 4.9,
                'stock': 35,
                'image': 'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400'
            },
            {
                'title': 'The 7 Habits of Highly Effective People',
                'author': 'Stephen R. Covey',
                'price': 499.00,
                'description': 'Powerful lessons in personal change. A holistic approach to solving personal and professional problems.',
                'category': 4,
                'isbn': '9781982137274',
                'publisher': 'Simon & Schuster',
                'year': 2020,
                'pages': 464,
                'rating': 4.7,
                'stock': 28,
                'image': 'https://images.unsplash.com/photo-1521714161819-15534968fc5f?w=400'
            },
            {
                'title': 'Think and Grow Rich',
                'author': 'Napoleon Hill',
                'price': 399.00,
                'description': 'The timeless classic on wealth creation. The 13 proven steps to riches.',
                'category': 4,
                'isbn': '9781585424337',
                'publisher': 'TarcherPerigee',
                'year': 2005,
                'pages': 320,
                'rating': 4.6,
                'stock': 20,
                'image': 'https://images.unsplash.com/photo-1523413363574-c30aa1c2a516?w=400'
            },
            
            # Business & Finance
            {
                'title': 'Rich Dad Poor Dad',
                'author': 'Robert T. Kiyosaki',
                'price': 549.00,
                'description': 'What the rich teach their kids about money that the poor and middle class do not.',
                'category': 7,
                'isbn': '9781612680194',
                'publisher': 'Plata Publishing',
                'year': 2017,
                'pages': 336,
                'rating': 4.7,
                'stock': 40,
                'image': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=400'
            },
            {
                'title': 'The Intelligent Investor',
                'author': 'Benjamin Graham',
                'price': 799.00,
                'description': 'The definitive book on value investing. A book of practical counsel.',
                'category': 7,
                'isbn': '9780060555665',
                'publisher': 'Harper Business',
                'year': 2006,
                'pages': 640,
                'rating': 4.8,
                'stock': 16,
                'image': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=400'
            },
            
            # Competitive Exams
            {
                'title': 'Quantitative Aptitude for Competitive Examinations',
                'author': 'R.S. Aggarwal',
                'price': 649.00,
                'description': 'Comprehensive guide for banking, SSC, and other competitive exams.',
                'category': 5,
                'isbn': '9789352602858',
                'publisher': 'S. Chand',
                'year': 2018,
                'pages': 1112,
                'rating': 4.5,
                'stock': 50,
                'image': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=400'
            },
            
            # Non-Fiction
            {
                'title': 'Sapiens',
                'author': 'Yuval Noah Harari',
                'price': 699.00,
                'description': 'A brief history of humankind. From the Stone Age to the Silicon Age.',
                'category': 3,
                'isbn': '9780062316110',
                'publisher': 'Harper',
                'year': 2015,
                'pages': 464,
                'rating': 4.8,
                'stock': 32,
                'image': 'https://images.unsplash.com/photo-1476275466078-4007374efbbe?w=400'
            },
            {
                'title': 'Educated',
                'author': 'Tara Westover',
                'price': 599.00,
                'description': 'A memoir about a young woman who leaves her survivalist family to pursue education.',
                'category': 3,
                'isbn': '9780399590504',
                'publisher': 'Random House',
                'year': 2018,
                'pages': 334,
                'rating': 4.7,
                'stock': 24,
                'image': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400'
            },
            
            # Children's Books
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J.K. Rowling',
                'price': 449.00,
                'description': 'The magical journey begins. Join Harry as he discovers he\'s a wizard.',
                'category': 6,
                'isbn': '9780439708180',
                'publisher': 'Scholastic',
                'year': 1999,
                'pages': 309,
                'rating': 4.9,
                'stock': 45,
                'image': 'https://images.unsplash.com/photo-1621351183012-e2f9972dd9bf?w=400'
            },
            {
                'title': 'The Little Prince',
                'author': 'Antoine de Saint-Exupéry',
                'price': 299.00,
                'description': 'A timeless tale about love, loss, and the importance of seeing with the heart.',
                'category': 6,
                'isbn': '9780156012195',
                'publisher': 'Harcourt',
                'year': 2000,
                'pages': 96,
                'rating': 4.8,
                'stock': 38,
                'image': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400'
            }
        ]
        
        for book_data in books_data:
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                price=book_data['price'],
                description=book_data['description'],
                category_id=categories[book_data['category']].id,
                isbn=book_data['isbn'],
                publisher=book_data['publisher'],
                published_year=book_data['year'],
                pages=book_data['pages'],
                rating=book_data['rating'],
                stock=book_data['stock'],
                image_url=book_data['image']
            )
            db.session.add(book)
        
        db.session.commit()
        print("✅ Sample books created")
        
        print("\n🎉 Database initialized successfully!")
        print("\n📋 Login Credentials:")
        print("Admin: admin@ebookworm.com / admin123")
        print("User: john@example.com / password123")

if __name__ == '__main__':
    init_database()
