from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class QuoteForm(FlaskForm):
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
    submit = SubmitField("Request Quote!")
