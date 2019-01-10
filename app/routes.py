from datetime import datetime
from datetime import timedelta

from flask import request, session, render_template, url_for, flash, redirect, abort
from app import app, db
from app.forms import QuoteForm
from app.models import Quote


@app.context_processor
def inject_app_debug():
    return dict(_debugging=app.debug)


@app.route("/")
@app.route("/index")
def index():
    # Demonstrate app logging
    app.logger.info(f"Request received for '/'!")
    return render_template("index.html")


@app.route("/get-a-quote", methods=["GET", "POST"])
def get_a_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        dt_now = datetime.utcnow()
        # Security consideration: rate limiting implementation
        if "last_quote" in session:
            # Calculate the time difference between now and the last quote
            last_quote_timedelta = dt_now - session["last_quote"]
            if last_quote_timedelta < timedelta(seconds=60):
                # Rate limit the quote request: flash rate limit warning and return the form unsubmitted
                flash("Quote request not added to database: rate-limited for attempting "
                      f"to request a quote within 1 minute of the last request at {session['last_quote']}.")
                return render_template("get_quote.html", title="Get a Quote!", form=form)

        # Filter quotes by email address specified in the form
        quotes_for_email = Quote.query.filter_by(email=form.email.data)
        # Get the count of previous quotes for email
        quotes_count = quotes_for_email.count()
        if quotes_count >= 5:
            # Log a warning that this email has made quotes_count previous quote requests
            app.logger.warning(f"{quotes_count} previous quotes for {form.email.data} at {last_quote._datetime}")

        quote = Quote(email=form.email.data,
                      forename=form.forename.data, surname=form.surname.data, telephone=form.telephone.data,
                      account_number=form.account_number.data, sort_code=form.sort_code.data,
                      address=form.address.data, town=form.town.data, postcode=form.postcode.data,
                      _datetime=dt_now)
        db.session.add(quote)
        db.session.commit()
        flash("Quote request added to database!")
        # Set information in session and goto thanks
        session["last_quote"] = dt_now
        session["email"] = form.email.data
        session["forename"] = form.forename.data
        return redirect(url_for("thanks"))
    elif form.is_submitted():
        app.logger.info(f"{type(form).__name__} validation failure by "
                        f"{request.remote_addr} with {request.user_agent}: {form.errors}")

    return render_template("get_quote.html", title="Get a Quote!", form=form)


@app.route("/thanks")
def thanks():
    if "email" in session and "forename" in session:
        email, forename = session["email"], session["forename"]
        main = f"Thanks {forename}!"
        small = f"Quote request received! We'll send an email to {email} after we have reviewed your quote request!"
        return render_template("200.html", main=main, small=small)
    # Abort to 410 GONE with explanation that the session is gone (cookies probably rejected or deleted)
    abort(410)


@app.route("/about")
def about():
    text = "Under construction by dwms" if app.debug else "Constructed by dwms"
    return render_template("about.html", title="About!", text=text)


@app.route("/_test_404")
def _test_404():
    abort(404)


@app.route("/_test_500")
def _test_500():
    abort(500) if app.debug else abort(404)
