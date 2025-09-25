import os
import sys
import subprocess

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware

# Add the outer Poetry folder to PYTHONPATH so Python can find the inner Django package
project_root = os.path.dirname(os.path.abspath(__file__))  # fullstack-projects folder

frontend_dir = os.path.join(project_root, "flask_task_manager", "frontend")

subprocess.Popen(
    ["npm", "start"],
    cwd=frontend_dir,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# Django
sys.path.insert(0, os.path.join(project_root, "django_tutorial"))

# Flask
sys.path.insert(0, os.path.join(project_root, "flask_task_manager"))

# FastAPI outer folder (contains the package)
sys.path.insert(0, os.path.join(project_root, "housing-analytics-api"))

# Import Django WSGI application
from django_tutorial.wsgi import get_wsgi_application  # inner package
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_tutorial.settings")
django_app = get_wsgi_application()

# Import Flask app
from flask_task_manager.backend.app import app as flask_app

# Import FastAPI app and wrap in WSGI
from housing_analytics_api.main import app as fastapi_app
fastapi_wsgi = WSGIMiddleware(fastapi_app)

# Combine all apps under DispatcherMiddleware
application = DispatcherMiddleware(
    django_app,  # default /
    {
        "/flask": flask_app,
        "/fastapi": fastapi_wsgi,
    }
)

# Optional: run locally
if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        "0.0.0.0",
        8000,
        application,
        use_reloader=True,
        use_debugger=True,
    )
