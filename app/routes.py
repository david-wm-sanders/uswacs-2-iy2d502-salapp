from datetime import datetime as dt

from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import QuoteForm
from app.models import Quote

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
        quote = Quote(email=form.email.data,
                      forename=form.forename.data, surname=form.surname.data, telephone=form.telephone.data,
                      account_number=form.account_number.data, sort_code=form.sort_code.data,
                      address=form.address.data, town=form.town.data, postcode=form.postcode.data,
                      _datetime=dt.utcnow())
        db.session.add(quote)
        db.session.commit()
        flash("Quote request received!")
        # return redirect(url_for("thanks"))
    return render_template("get_quote.html", title="Get a Quote!", form=form)

@app.route("/about")
def about():
    return "<p>Under construction by dwms</p>"
