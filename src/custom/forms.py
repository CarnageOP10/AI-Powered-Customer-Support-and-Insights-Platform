from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class RaiseForm(FlaskForm):
    name = StringField(label='Name:', validators=[Length(min=2, max=50), DataRequired()])
    mo_number = StringField(label='MobileNumber:', validators=[Length(min=10, max=10), DataRequired()])
    state_name = StringField(label='StateName:', validators=[Length(min=2, max=50), DataRequired()])
    city_name = StringField(label='CityName:', validators=[Length(min=2, max=50), DataRequired()])
    pincode = StringField(label='Pincode:', validators=[Length(min=6, max=6), DataRequired()])
    complain = StringField(label='Complain:', validators=[Length(min=10, max=5000), DataRequired()])
    submit = SubmitField(label='Raise Alert')