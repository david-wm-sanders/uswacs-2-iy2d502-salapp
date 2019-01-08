from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email

from app.models import Quote


class QuoteForm(FlaskForm):
    # Define internal variables that grab the column length from the Quote model
    # Figure out a way to refactor this - try to subclass FlaskForm perhaps?
    _maxlen_email = Quote.email.property.columns[0].type.length
    _maxlen_forename = Quote.forename.property.columns[0].type.length
    _maxlen_surname = Quote.surname.property.columns[0].type.length
    _maxlen_telephone = Quote.telephone.property.columns[0].type.length
    _maxlen_account_number = Quote.account_number.property.columns[0].type.length
    _maxlen_sort_code = Quote.sort_code.property.columns[0].type.length
    _maxlen_address = Quote.address.property.columns[0].type.length
    _maxlen_town = Quote.town.property.columns[0].type.length
    _maxlen_postcode = Quote.postcode.property.columns[0].type.length

    # TODO: Add better ALERT (warning) logging on validation failure, currently handled in route
    # TODO: SQL injection check - validate for possible SQL injection strings, ALERT, and reject with funny message
    # TODO: Password complexity and (basic) not in wordlist validation for relevant forms

    # Define form fields
    # TODO: Derive custom LengthedStringField that adds length validation and sets HTML maxlength attribute
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=_maxlen_email)],
                        render_kw={"maxlength": _maxlen_email})
    forename = StringField("Forename", validators=[DataRequired(), Length(max=_maxlen_forename)],
                        render_kw={"maxlength": _maxlen_forename})
    surname = StringField("Surname", validators=[DataRequired(), Length(max=_maxlen_surname)],
                        render_kw={"maxlength": _maxlen_surname})
    telephone = StringField("Telephone", validators=[DataRequired(), Length(max=_maxlen_telephone)],
                        render_kw={"maxlength": _maxlen_telephone})
    account_number = StringField("Account Number", validators=[DataRequired(), Length(max=_maxlen_account_number)],
                        render_kw={"maxlength": _maxlen_account_number})
    sort_code = StringField("Sort Code", validators=[DataRequired(), Length(max=_maxlen_sort_code)],
                        render_kw={"maxlength": _maxlen_sort_code})
    address = StringField("Address", validators=[DataRequired(), Length(max=_maxlen_address)],
                        render_kw={"maxlength": _maxlen_address})
    town = StringField("Town", validators=[DataRequired(), Length(max=_maxlen_town)],
                        render_kw={"maxlength": _maxlen_town})
    postcode = StringField("Postcode", validators=[DataRequired(), Length(max=_maxlen_postcode)],
                        render_kw={"maxlength": _maxlen_postcode})
    # DEBUG: disable recaptcha for development and testing, use a HiddenField to represent it in the template
    # recaptcha = RecaptchaField()
    recaptcha = HiddenField()
    submit = SubmitField("Request Quote!")
