# Fruit App - Django Backend with Frontend

A simple web application for displaying fruit data, built with Django as a backend API and Vanilla JavaScript as frontend.

## 📋 Project Overview

The Fruit App is a learning and demonstration application that provides a REST API for fruit data. The project consists of a Django backend that delivers JSON data about various fruits, and a simple HTML/JavaScript frontend for displaying this data.

## 🚀 Technologies Used

### Backend
- **Django 5.2.7** - Python Web Framework
- **django-cors-headers 4.9.0** - For Cross-Origin Resource Sharing (CORS)
- **SQLite** - Default database (integrated via Django)

### Frontend
- **HTML5** - Web page structure
- **Vanilla JavaScript** - For API calls and DOM manipulation
- **CSS** - Simple styling for table display

## 📁 Project Structure

```
da-intensivkurs-backend-fruit-app/
├── core/                    # Django project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── fruit_app/              # Django app for fruits
│   ├── views.py           # API endpoints
│   ├── urls.py            # App-specific URLs
│   └── models.py          # Data models (currently empty)
├── fruit_app_frontend/     # Frontend files
│   ├── index.html         # Main HTML file
│   └── script.js          # JavaScript for API calls
├── db.sqlite3             # SQLite database file
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.8+ installed
- pip (Python Package Manager)

### 1. Clone repository
```bash
git clone <repository-url>
cd da-intensivkurs-backend-fruit-app
```

### 2. Create virtual environment (recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Django project
```bash
python manage.py runserver
```

The server runs by default on `http://127.0.0.1:8000/`

## 📖 Usage

### Backend API

**GET `/fruits/`**
- Returns a JSON list of all fruits
- Example URL: `http://127.0.0.1:8000/fruits/`

Example Response:
```json
[
    {"name": "Apple", "color": "Red", "weight": "150g"},
    {"name": "Banana", "color": "Yellow", "weight": "120g"},
    {"name": "Orange", "color": "Orange", "weight": "130g"}
    // ... more fruits
]
```

### Frontend

1. Start Django server (see Installation)
2. Open `fruit_app_frontend/index.html` in a web browser
3. Fruits will be automatically displayed in a table

**Note:** The frontend must be opened separately as it is not served through Django.

## ⚙️ Key Features

- **REST API**: Simple GET endpoints for fruit data
- **CORS Support**: Enables frontend-backend communication
- **Responsive Design**: Simple but functional frontend design
- **Asynchronous Data Loading**: JavaScript fetch API for smooth user experience
- **Error Handling**: 404 errors for invalid requests

## 🔧 Development

### Adding New Fruits
Edit the `fruits` list in `fruit_app/views.py`:

```python
fruits = [
    {"name": "New Fruit", "color": "Color", "weight": "Weight"},
    # ... existing fruits
]
```

### Adjusting CORS Settings
The CORS configuration is located in `core/settings.py` and is already set up for local development.

## 🤝 Contributing

This is a learning project from a backend intensive course. For improvements or extensions:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Create a pull request

## 📞 Support

For questions about the project or installation problems, create an issue in the repository or contact the course instructor.