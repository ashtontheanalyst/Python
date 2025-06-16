from flask import Flask, render_template, url_for

# Create an instance of the app from Flask
app = Flask(__name__)

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

# This runs the app, debug mode shos us errors if they happen
if __name__ == '__main__':
    app.run(debug=True)