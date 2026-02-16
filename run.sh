#!/bin/bash

# E-BookWorm Startup Script

echo "🚀 Starting E-BookWorm..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Check if database exists
if [ ! -f "database.db" ]; then
    echo "🗄️  Initializing database..."
    python init_db.py
fi

# Run the application
echo ""
echo "✅ Starting Flask application..."
echo "🌐 Open http://localhost:5000 in your browser"
echo ""
echo "Demo Accounts:"
echo "  Admin: admin@ebookworm.com / admin123"
echo "  User: john@example.com / password123"
echo ""
python app.py
