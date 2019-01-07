from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email

class QuoteForm(FlaskForm):
    # TODO: Add more validation, such as length checking (ideally with lens pulled from Quote model for SRP)
    email = StringField("Email", validators=[DataRequired(), Email()])
    # password = PasswordField("Password:", validators=[DataRequired()])
    forename = StringField("Forename", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    telephone = StringField("Telephone", validators=[DataRequired()])
    account_number = StringField("Account Number", validators=[DataRequired()])
    sort_code = StringField("Sort Code", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    town = StringField("Town", validators=[DataRequired()])
    postcode = StringField("Postcode", validators=[DataRequired()])
    # DEBUG: disable recaptcha for development and testing, use a HiddenField to represent it in the template
    # recaptcha = RecaptchaField()
    recaptcha = HiddenField()
    submit = SubmitField("Request Quote!")
