from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import ValidationError

from app import app
from app.models import Quote


class ModelLengthValidator:
    """Validates field length from SQLAlchemy property type length"""
    def __init__(self, model_field, minimum_length=0):
        self._min_length = minimum_length
        try:
            self._max_length = model_field.property.columns[0].type.length
        except AttributeError as e:
            raise Exception("Does this model_field have a length for validation?") from e

    def __call__(self, form, field):
        field_data_length = field.data and len(field.data) or 0
        if field_data_length < self._min_length:
            return ValidationError(f"Field cannot be less than {self._min_length} characters long.")
        if field_data_length > self._max_length:
            raise ValidationError(f"Field cannot be more than {self._max_length} characters long.")


class ModelStringField(StringField):
    def __init__(self, label="", validators=None, model_field=None, **kwargs):
        self._max_length = model_field.property.columns[0].type.length
        super(StringField, self).__init__(label, validators, **kwargs)

    def __call__(self, **kwargs):
        if "maxlength" not in kwargs:
            kwargs["maxlength"] = self._max_length
        return super(StringField, self).__call__(**kwargs)


class QuoteForm(FlaskForm):
    # TODO: Add better ALERT (warning) logging on validation failure, currently handled in route
    # TODO: SQL injection check - validate for possible SQL injection strings, ALERT, and reject with funny message
    # TODO: Password complexity and (basic) not in wordlist validation for relevant forms

    # Define form fields
    email = ModelStringField("Email", validators=[DataRequired(), Email(), ModelLengthValidator(Quote.email)],
                             model_field=Quote.email)
    forename = ModelStringField("Forename", validators=[DataRequired(), ModelLengthValidator(Quote.forename)],
                                model_field=Quote.forename)
    surname = ModelStringField("Surname", validators=[DataRequired(), ModelLengthValidator(Quote.surname)],
                               model_field=Quote.surname)
    telephone = ModelStringField("Telephone", validators=[DataRequired(), ModelLengthValidator(Quote.telephone)],
                                 model_field=Quote.telephone)
    account_number = ModelStringField("Account Number", validators=[DataRequired(),
                                                                    ModelLengthValidator(Quote.account_number)],
                                      model_field=Quote.account_number)
    sort_code = ModelStringField("Sort Code", validators=[DataRequired(), ModelLengthValidator(Quote.sort_code)],
                                 model_field=Quote.sort_code)
    address = ModelStringField("Address", validators=[DataRequired(), ModelLengthValidator(Quote.address)],
                               model_field=Quote.address)
    town = ModelStringField("Town", validators=[DataRequired(), ModelLengthValidator(Quote.town)],
                            model_field=Quote.town)
    postcode = ModelStringField("Postcode", validators=[DataRequired(), ModelLengthValidator(Quote.postcode)],
                                model_field=Quote.postcode)
    # DEBUG: disable recaptcha for development and testing, use a HiddenField to represent it in the template
    # recaptcha = RecaptchaField()
    recaptcha = HiddenField()
    submit = SubmitField("Request Quote!")
