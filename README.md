# Django Backend - Managed Content Sites

## Overview
This is a Fullstack Django Project template designed with a Bootstrap-based frontend. It includes preset configurations for a scalable django project.

It has a prebuilt authentication system with a custom user model (Account). Just duplicate and you're off to the races

## Features
- **Modular Apps** under `core/apps`
- **Media & Static File Handling**
- **Environment Configuration** using `.env`
- **Database Configuration** in `db.py-tpl`


## Folder Structure
```
fsa_project_root/
│── core/
│   ├── apps/      # Modular Django apps
│   	├── account/		# Custom authentication app
│   	├── django_fsa_app.zip		# Template for creating special apps
│   ├── cdn/       # Static & media storage
│   ├── boilerplates/       # Code boilerplates + Bootstrap
│   ├── media/     # Media files
│   ├── static/    # Static files
│   ├── templates/ # Frontend template files
│── project_name/
│   ├── __init__.py-tpl
│   ├── settings.py-tpl  # Django settings template
│   ├── context_processors.py-tpl  # Frontend context
│   ├── urls.py-tpl      # URL routing template
│   ├── wsgi.py-tpl      # WSGI application setup
│   ├── asgi.py-tpl      # ASGI application setup
│   ├── db.py-tpl        # Database connection setup
│── .env                 # Environment variables
│── manage.py-tpl        # Django management script
```

## Installation & Setup
```sh
# Install dependencies
pip install -r requirements.txt

# Create a project
cd ..
django-admin startproject <project_name> --template fsa_project_root

# Set Postgresql database details in .env file
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=

# Make migrations (neccesary for the account module)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

