from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField 
from wtforms.validators import DataRequired,Email,Length

#here messages  are custom messeges created by us
class RegistrationForm(FlaskForm):
    name=StringField("Full Name",validators=[DataRequired(message="name cannot be empty")])
    email=StringField("Email",validators=[DataRequired(),Email(message="pls enter valid email")])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=6)])
    submit=SubmitField("Register")