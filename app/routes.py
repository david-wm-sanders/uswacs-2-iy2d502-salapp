from flask import render_template, flash, redirect
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
def quote():
    form = QuoteForm()
    if form.validate_on_submit():
        flash("Quote request received!")
        # return redirect("/thanks")
    return render_template("get_quote.html", title="Get a Quote!", form=form)
