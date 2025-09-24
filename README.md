# fullstack-projects
full stack projects
parent umbrella project for full stack apps

Fullstack Projects

This repository is an umbrella project that demonstrates multiple full-stack web applications built with Django, Flask, and FastAPI.
All apps are deployed together under one service on Render

Live Demo (Render)
Django app → /
Flask app → /flask
FastAPI app → /fastapi

Example:
https://your-app.onrender.com/ → Django
https://your-app.onrender.com/flask → Flask
https://your-app.onrender.com/fastapi → FastAPI

fullstack-projects/
├─ django-tutorial/          # Django project
│   ├─ manage.py
│   └─ django_tutorial/...
├─ flask_task_manager/           # Flask project
│   └─ app.py
├─ housing-analytics-api /         # FastAPI project
│   └─ main.py
├─ fullstack-projects_wsgi.py   # WSGI/ASGI wrapper combining all apps
├─ pyproject.toml       # Poetry dependencies
└─ README.md

Local Development
Requirements
Python 3.11+
Poetry

poetry add flask@^3.1 flask-sqlalchemy@^3.0 flask-pymongo@^3.0 flask-cors@^4.0
poetry install
source "$(poetry env info --path)/bin/activate"


Run locally
gunicorn fullstack_projects_wsgi:application --reload

Open in your browser:

Django → http://localhost:8000/
Flask → http://localhost:8000/flask
FastAPI → http://localhost:8000/fastapi

Deployment (Render)
Build Command
poetry install

Start Command
 PYTHONPATH=django-tutorial gunicorn fullstack_projects_wsgi:applicationTech Stack
Django 5 (classic fullstack framework)
Flask 2 (lightweight microframework)
FastAPI (modern async framework for APIs)
Gunicorn with DispatcherMiddleware to serve them all in one service