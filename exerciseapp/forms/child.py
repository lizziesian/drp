from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from exerciseapp.models.user import User, ChildUser, ParentUser

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min=2, max=20)])
    name = StringField("Name", validators = [DataRequired(), Length(min=2, max=20)])
    parent_code = IntegerField("Parent Invite Code", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")

    def validate_parent_code(self, parent_code):
        parent = ParentUser.query.filter_by(id=parent_code.data).first()
        if not parent:
            raise ValidationError("Incorrect parent code. No parent account exists.")

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
