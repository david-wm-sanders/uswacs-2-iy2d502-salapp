from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import QuoteForm

@app.route("/")
@app.route("/index")
def index():
    # Demonstrate app logging
    app.logger.info(f"Request received for '/'!")
    user = {"username": "dwms"}
    quotes = [{"email": "d@w.local", "forename": "D", "surname": "W"},
              {"email": "m@s.local", "forename": "M", "surname": "S"}]
    return render_template("index.html", user=user, quotes=quotes)

@app.route("/get-a-quote", methods=["GET", "POST"])
def get_a_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        flash("Quote request received!")
        # return redirect(url_for("thanks"))
    return render_template("get_quote.html", title="Get a Quote!", form=form)

@app.route("/about")
def about():
    return "<p>Under construction by dwms</p>"
