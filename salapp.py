"""Set up application to be used by 'flask run'."""
from app import app, db
from app.models import Quote


@app.shell_context_processor
def make_shell_context():
    """Add context objects for 'flask shell'."""
    return {"db": db, "Quote": Quote}
