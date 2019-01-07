from datetime import datetime as dt
from datetime import timedelta

from flask import request, render_template, url_for, flash, redirect
from app import app, db
from app.forms import QuoteForm
from app.models import Quote

@app.route("/")
@app.route("/index")
def index():
    # Demonstrate app logging
    app.logger.info(f"Request received for '/'!")
    # TODO: Make beautiful index page or just redirect to url_for('get_a_quote') automatically
    user = {"username": "dwms"}
    quotes = [{"email": "d@w.local", "forename": "D", "surname": "W"},
              {"email": "m@s.local", "forename": "M", "surname": "S"}]
    return render_template("index.html", user=user, quotes=quotes)

@app.route("/get-a-quote", methods=["GET", "POST"])
def get_a_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        # Security consideration: rate limiting implementation
        # Filter quotes by email address specified in the form
        quotes_for_email = Quote.query.filter_by(email=form.email.data)
        # Find the last quote for email address, None if no previous quotes have been requested for the email address
        last_quote = quotes_for_email.order_by(Quote._datetime.desc()).first()
        if last_quote:
            # Calculate the time difference between now and the last quote
            last_quote_timedelta = dt.utcnow() - last_quote._datetime
            if last_quote_timedelta < timedelta(seconds=10):
                # Rate limit the quote request: flash rate limit warning and return the form unsubmitted
                flash("Quote request not added to database: rate-limited for attempting " \
                      f"to request a quote within 10 seconds of the last request at {last_quote._datetime}")
                return render_template("get_quote.html", title="Get a Quote!", form=form)
            if quotes_for_email.count() >= 5:
                # Log a warning that this email has made quotes_count previous quote requests
                app.logger.warning(f"{quotes_count} previous quotes for {form.email.data} at {last_quote._datetime}")

        quote = Quote(email=form.email.data,
                      forename=form.forename.data, surname=form.surname.data, telephone=form.telephone.data,
                      account_number=form.account_number.data, sort_code=form.sort_code.data,
                      address=form.address.data, town=form.town.data, postcode=form.postcode.data,
                      _datetime=dt.utcnow())
        db.session.add(quote)
        db.session.commit()
        flash("Quote request added to database!")
        # TODO: Set information in session
        # TODO: Implement a thanks page
        # return redirect(url_for("thanks"))
    elif form.is_submitted():
        app.logger.warning(f"{type(form).__name__} validation failure by " \
                           f"{request.remote_addr} with {request.user_agent}: {form.errors}")

    return render_template("get_quote.html", title="Get a Quote!", form=form)

@app.route("/about")
def about():
    text = "Under construction by dwms" if app.debug else "Constructed by dwms"
    return render_template("about.html", text=text)
