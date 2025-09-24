import os
import subprocess
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# ---------------------------
# Start frontend automatically
# ---------------------------
frontend_dir = "/common/projects/python/fullstack-projects/flask_task_manager/frontend"

subprocess.Popen(
    ["npm", "start"],
    cwd=frontend_dir,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# ---------------------------
# Import your existing Flask backend
# ---------------------------
from flask_task_manager.backend.app import app  # use your real variable as-is

# ---------------------------
# Combine apps with DispatcherMiddleware
# ---------------------------
application = DispatcherMiddleware(
    None,
    {
        "/flask": app,  # Flask backend API
    }
)

# ---------------------------
# Optional: local development server
# ---------------------------
if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        "0.0.0.0",
        8000,
        application,
        use_reloader=True,
        use_debugger=True,
    )
