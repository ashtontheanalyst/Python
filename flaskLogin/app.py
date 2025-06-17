from flask import Flask, render_template, url_for                   # Packages for main site/app
from flask_sqlalchemy import SQLAlchemy                             # This is for our DB
from flask_login import UserMixin                                   # This helps build out the table in the DB
# For our login and register forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, length, ValidationError
# For passwords
from flask_bcrypt import bcrypt

# INTIALIZATION -------------------------------------------------------------------------------------
# Create an instance of the app from Flask
app = Flask(__name__)

# Encryption init
bcrypt = bcrypt(app)

# Database configuration and then initialization    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'         # Links the DB instance to our file
app.config['SECRET_KEY'] = 'totallyasecret'                             # This is our session cookie
db = SQLAlchemy(app)                                                    # Creates the instance 

# Building the DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)                        # Identity column
    username = db.Column(db.String(20), nullable=False, unique=True)    # User and pass with max chars, can't be empty, users unique
    password = db.Column(db.String(80), nullable=False)

'''
In order to get the db fully working, follow these steps:
    - Open a terminal and enter a python shell: python, py, or python3
    - Copy and paste this code into that terminal:

from app import app, db, User

with app.app_context():
    db.create_all()
    print(User.query.all())
    
    - The output should show no users like this: []
    - The db is going to be created in a new folder called 'instance'
    - You can double check by running this in the folder housing the db:
        sqlite3 database.db
        .tables
'''


# Registration Form ---------------------------------------------------------------------------------
class RegisterForm(FlaskForm):
    username = StringField(validators=[input_required(), length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    # The reason why the db password allows 80 chars is because this max of
    # 20 char one will be hashed
    password = PasswordField(validators=[input_required(), length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Register")

    # Making sure the username isn't already in user and if so showing an error
    def validate_username(self, username):
        # Query the db table and seeing if there's an exact username match
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists and is in use. Please choose another.")


# Login Form ----------------------------------------------------------------------------------------
# Pretty much the same as the register page but without the db user check
class LoginForm(FlaskForm):
    username = StringField(validators=[input_required(), length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    # The reason why the db password allows 80 chars is because this max of
    # 20 char one will be hashed
    password = PasswordField(validators=[input_required(), length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField("Login")


# PAGES ---------------------------------------------------------------------------------------------
# This is the URL route for the home page, the landing page
@app.route('/')
def home():
    # Returns the html page 'home.html' from the templats folder automatically
    return render_template('home.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()                                  # This is our login function seen above
    return render_template('login.html', form=form)     # Pass our form into html form

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)


# RUN ----------------------------------------------------------------------------------------------
# This runs the app, debug mode shos us errors if they happen
if __name__ == '__main__':
    app.run(debug=True)