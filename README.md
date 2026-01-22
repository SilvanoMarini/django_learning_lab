# Django Learning Lab

This repository is a personal learning lab created to study and practice the fundamentals of **Django**, following a structured course curriculum.

The project is not intended to be a production-ready application. Its purpose is to progressively apply Django concepts as they are introduced during the course, serving as a hands-on study environment.

## 🎯 Purpose

- Learn Django from scratch
- Understand Django’s request/response cycle
- Practice views, URLs, templates, and static files
- Apply Django concepts incrementally through guided lessons
- Consolidate backend fundamentals using a real framework

## 📚 Course Content Covered

The following topics are studied and implemented throughout this repository:

- Creating a Django project using `django-admin startproject`
- Understanding Django’s core files and project structure
- Introduction to Django (high-level overview)
- `django-admin` and `manage.py`
- Function-based views
- `HttpRequest`, `HttpResponse`, and HTTP status codes
- Request → Response flow in Django
- Creating apps with `manage.py startapp`
- Organizing views inside apps
- URL routing with `path`, `include`, and app-level `urls.py`
- Rendering HTML with `render`
- Templates configuration and `INSTALLED_APPS`
- Template inheritance using `extends` and blocks
- Partials and reusable templates with `include`
- Static files configuration:
  - `STATIC_URL`
  - `STATICFILES_DIRS`
  - `{% load static %}`
- Passing data to templates using context
- Dynamic URLs in Django views and templates
- Global CSS structure
- Template loops (`for`)
- Conditional rendering (`if`, `elif`, `else`)
- Dynamic URL dispatcher behavior
- Static and dynamic URL usage
- Single post pages and custom views
- Custom 404 error handling with `Http404`
- Basic styling and navigation layout
- Understanding `DEBUG` and `ALLOWED_HOSTS` (development vs production)

## 🛠 Technologies

- Python
- Django
- SQLite (default Django database)
- HTML
- CSS

## 📂 Project Structure

The repository follows Django’s standard project and app structure.  
Files and folders may change as new lessons are completed and concepts are refined.

### Apps
- **home**: Handles the homepage with a welcome message.
- **blog**: Manages blog posts, including listing and individual post views. Currently uses hardcoded data from `blog/data.py` instead of Django models.
- **base**: Contains global templates (e.g., base.html, partials) and static files (CSS) shared across the project.

## ✨ Current Features

- **Homepage**: Simple welcome page at the root URL.
- **Blog Index**: Displays a list of posts with titles and summaries.
- **Post Details**: Individual pages for each post, accessible via dynamic URLs.
- **Navigation**: Basic menu and layout using template inheritance.
- **Styling**: Global CSS for responsive design and basic aesthetics.
- **Error Handling**: Custom 404 for non-existent posts.

*Note: Data is currently mocked; future updates may introduce real models and database integration.*

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/SilvanoMarini/django_learning_lab.git
```

### 2. Navigate to the project directory
```bash
cd django-learning-lab
```

### 3. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 4. Install Django
```bash
pip install django
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open the browser and access
```text
http://127.0.0.1:8000/
```

## 🚧 Project Status

**In progress — study project**

This repository may include:

- Experimental code
- Refactors as learning evolves
- Non-final implementations

## 🧠 Notes

This project exists exclusively for educational purposes.
Code structure and patterns may change frequently as new Django concepts are introduced.

## 👤 Author

Silvano Junior  
Software Engineering Student  
Backend-focused learner  