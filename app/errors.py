"""Set up error handlers for salapp."""
from flask import render_template
from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    """Return rendered template for status code 404."""
    return render_template("404.html"), 404


@app.errorhandler(410)
def gone_error(error):
    """Return rendered template for status code 410."""
    return render_template("410.html"), 410


@app.errorhandler(500)
def internal_error(error):
    """Rollback database and return rendered template for status code 500."""
    db.session.rollback()
    return render_template("500.html"), 500
