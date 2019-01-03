from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "dwms"}
    quotes = [{"email": "d@w.local", "forename": "D", "surname": "W"},
              {"email": "m@s.local", "forename": "M", "surname": "S"}]
    return render_template("index.html", user=user, quotes=quotes)
    # return render_template("index.html", title="Home", user=user)
