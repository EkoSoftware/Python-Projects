from flask import Flask, render_template, redirect, url_for, request

from datetime import datetime
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.route("/hello/<name>")
def hello_there(name = None):
  return render_template(
    "hello_there.html",
    name=name,
    date=datetime.now()
  )


@app.route('/api/data')
def get_data():
  return app.send_static_file('data.json')


# Forms test
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import Form, BooleanField, StringField, SubmitField, RadioField, SelectField, validators
from wtforms.validators import DataRequired, Length, InputRequired
from flask_bootstrap import Bootstrap5
import secrets
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)

# Flask-WTF requires this line
csrf = CSRFProtect(app)

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])

  # radioval = RadioField(label="Hur gammal är du?", 
  #                       validators=[InputRequired(message="Välj en")],
  #                       choices=[ ("18-30","31-50","51+")])
                        
  # selectval = SelectField(label="Vad äter du?",
  #                         choices=[ ("Hamburgare", "Pizza", "Chips") ])

class User():
  def __init__(self, username, email, isvalid):
    self.username = username
    self.email = email
    self.isvalid = False
    
  
users = []

@app.route('/test', methods=['GET', 'POST'])
def test():
  thisForm = RegistrationForm()  
  return render_template('test.html', form=thisForm, title='Register')
  