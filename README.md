# Fruit App - Django Full-Stack Application

A full-stack web application for displaying fruit data, built with Django using server-side rendering.

## 📋 Project Overview

The Fruit App is a learning and demonstration application built with Django. The project uses Django's template system to render HTML pages that display fruit data directly from the backend, providing a simple and integrated full-stack solution. The project is organized into separate backend and frontend directories for better code organization.

## 🚀 Technologies Used

### Backend
- **Django 5.2.7** - Python Web Framework
- **Django Templates** - Server-side rendering
- **django-cors-headers 4.9.0** - For Cross-Origin Resource Sharing (CORS)
- **SQLite** - Default database (integrated via Django)

### Frontend
- **Django Template Language (DTL)** - Template rendering
- **HTML5** - Web page structure
- **CSS** - Styling for the application

## 📁 Project Structure

```
da-intensivkurs-backend-fruit-app/
├── backend/                 # Django backend application
│   ├── core/               # Django project configuration
│   │   ├── settings.py    # Django settings
│   │   ├── urls.py        # Main URL configuration
│   │   └── wsgi.py        # WSGI configuration
│   ├── fruit_app/         # Django app for fruits
│   │   ├── views.py       # Views and logic
│   │   ├── urls.py        # App-specific URLs
│   │   ├── models.py      # Data models
│   │   ├── templates/     # HTML templates
│   │   │   └── fruit_app/ # App-namespaced templates
│   │   └── static/        # Static files (CSS, JS, images)
│   │       └── fruit_app/ # App-namespaced static files
│   ├── db.sqlite3         # SQLite database file
│   ├── manage.py          # Django management script
│   └── requirements.txt   # Python dependencies
├── frontend/               # Optional standalone frontend files (Old files)
│   ├── index.html         # Static HTML (for reference)
│   └── script.js          # JavaScript (for reference)
└── README.md              # This file
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
cd backend
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


for testing with static files use:

python manage.py runserver --insecure
```

The server runs by default on `http://127.0.0.1:8000/`

## 📖 Usage

### Accessing the Application

1. Start the Django development server:
```bash
python manage.py runserver


for testing with static files use:

python manage.py runserver --insecure
```

2. Open your browser and navigate to:
   - Main page: `http://127.0.0.1:8000/fruits/`
   
3. The fruits will be displayed directly in the Django-rendered HTML page

**Note:** The application now uses Django's template system, so everything is served through Django on port 8000.

## ⚙️ Key Features

- **Django Templates**: Server-side rendering with Django Template Language
- **Integrated Full-Stack**: Backend and frontend served from a single Django application
- **Simple Data Display**: Clean table-based presentation of fruit data
- **Easy to Extend**: Add new fruits or modify templates easily
- **Error Handling**: Proper HTTP error responses
## 🔧 Development

### Adding New Fruits
Edit the `fruits` list in `backend/fruit_app/views.py`:

```python
fruits = [
    {"name": "Apfel", "weight": 100, "color": "Rot", "ordered": True},
    # ... existing fruits
]
```

### Modifying Templates
Edit the HTML templates in the `backend/fruit_app/templates/fruit_app/` directory to change the appearance or layout of the application.

### Adding Static Files
Add CSS, JavaScript, or image files to `backend/fruit_app/static/fruit_app/` and reference them in your templates using:
```django
{% load static %}
<link rel="stylesheet" href="{% static 'fruit_app/style.css' %}">
```

### CORS Settings
The CORS configuration is located in `backend/core/settings.py`. This may not be necessary anymore if you're only using Django templates without separate frontend API calls.

## 🤝 Contributing

This is a learning project from a backend intensive course. For improvements or extensions:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Create a pull request

## 📞 Support

For questions about the project or installation problems, create an issue in the repository or contact the course instructor.