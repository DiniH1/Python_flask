# Model View Controller (MVC) with Python Flask
## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps

```
# Creating a file called app.py
# Let's see how we can use Python Flask to interact with our browser

from flask import Flask
# We have to create an object of this class
app = Flask(__name__) # creating an app instance

# Let's create a function to link to our home//default page
# Let's connect this function to our browser
@app.route("/") # decorating our function with @app.route in our browser
def index():
    return " Welcome to Engineering 89 DevOps team"

# flask run
# Let's create a welcome page
@app.route("/welcome/")
def welcome():
    return "<h1> Welcome page for Flask app</h1>"

# Create a decorator to route traffic to login page
# Display 2 messages of your choice in from of h1 and h2

@app.route("/login/")
def log():
    return "<h1> Welcome to the login page </h1> <h2> Please enter your user login details </h2>"
```
