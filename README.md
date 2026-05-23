# Django Projects Portfolio

A curated collection of Django projects built while learning and practicing backend development, template rendering, CRUD workflows, forms, validations, API integration, and project organization.

This repository is structured as a multi-project Django portfolio. Each folder is an independent Django project with its own `manage.py`, apps, templates, migrations, and settings.

## Projects

| Project | Description | Highlights |
| --- | --- | --- |
| `book_crud` | Book details management system | Create, read, update, and delete books using Django models, views, templates, and URL routing |
| `student_project` | Student registration system | Form handling, field validation, file upload support, SQLite database integration, and success workflow |
| `api` | User listing API demo | Fetches external user data from JSONPlaceholder using `requests` and renders it in a Django template |
| `sample` | Education society website | Template inheritance, static assets, page routing, and simple dynamic data rendering |
| `email_project` | Email configuration and test mail app | Stores SMTP configuration through a Django form and sends test emails using Django's mail utilities |

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap/static assets
- Django Templates
- External API integration with `requests`

## Repository Structure

```text
Django-Projects/
  api/
  book_crud/
  email_project/
  sample/
  student_project/
```

## How To Run A Project

Clone the repository:

```bash
git clone https://github.com/Sathvika-g-29/Django-Projects.git
cd Django-Projects
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install Django and requests:

```bash
pip install django requests
```

Move into any project folder and run it:

```bash
cd student_project
python manage.py migrate
python manage.py runserver
```

Open the local server:

```text
http://127.0.0.1:8000/
```

## Project Entry Points

Some projects use specific URLs:

| Project | URL |
| --- | --- |
| `student_project` | `/register/` |
| `book_crud` | project root or configured book URLs |
| `api` | configured user listing route |
| `email_project` | `/email-config/` and `/send-test/` |
| `sample` | project root and app routes |

## What This Repository Demonstrates

- Building Django apps from scratch
- Creating models and database migrations
- Handling user input with Django forms
- Validating form data
- Uploading files through forms
- Implementing CRUD operations
- Rendering dynamic HTML templates
- Organizing reusable templates and static files
- Connecting Django views to external APIs
- Configuring email delivery with Django SMTP settings
- Keeping repositories clean with `.gitignore`

## Notes

Local-only files such as `db.sqlite3`, `__pycache__`, virtual environments, and uploaded media are intentionally ignored to keep the repository clean and portable.

Secrets such as Django `SECRET_KEY` values are configured through environment variables where applicable.

## Author

**Sathvika G**  
GitHub: [Sathvika-g-29](https://github.com/Sathvika-g-29)
