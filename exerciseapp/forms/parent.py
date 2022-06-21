from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from exerciseapp.models.user_parent import ParentUser

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min=2, max=20)])
    name = StringField("Name", validators = [DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = ParentUser.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
