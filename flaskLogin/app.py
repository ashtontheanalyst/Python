from flask import Flask, render_template, url_for                   # Packages for main site/app
from flask_sqlalchemy import SQLAlchemy                             # This is for our DB
from flask_login import UserMixin                                   # This helps build out the table in the DB

# INTIALIZATION -------------------------------------------------------------------------------------
# Create an instance of the app from Flask
app = Flask(__name__)

# Database configuration and then initialization    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'     # Links the DB instance to our file
app.config['SECRET_KEY'] = 'totallyasecret'                         # This is our session cookie
db = SQLAlchemy(app)                                                # Creates the instance 

# Building the DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)                    # Identity column
    username = db.Column(db.String(20), nullable=False)             # User and pass with max chars, can't be empty
    password = db.Column(db.String(80), nullable=False)


# PAGES ---------------------------------------------------------------------------------------------
# This is the URL route for the home page, the landing page
@app.route('/')
def home():
    # Returns the html page 'home.html' from the templats folder automatically
    return render_template('home.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Registration Page
@app.route('/register')
def register():
    return render_template('register.html')


# RUN ----------------------------------------------------------------------------------------------
# This runs the app, debug mode shos us errors if they happen
if __name__ == '__main__':
    app.run(debug=True)