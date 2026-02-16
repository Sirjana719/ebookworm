@echo off
echo.
echo 🚀 Starting E-BookWorm...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Install requirements
echo 📥 Installing dependencies...
pip install -q -r requirements.txt

REM Check if database exists
if not exist "database.db" (
    echo 🗄️  Initializing database...
    python init_db.py
)

REM Run the application
echo.
echo ✅ Starting Flask application...
echo 🌐 Open http://localhost:5000 in your browser
echo.
echo Demo Accounts:
echo   Admin: admin@ebookworm.com / admin123
echo   User: john@example.com / password123
echo.
python app.py
