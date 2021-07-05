# Creating a file called app.py
# Let's see how we can use Python Flask to interact with our browser

from flask import Flask, redirect, url_for, render_template
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
    return render_template("welcome.html")

# Create a decorator to route traffic to login page
# Display 2 messages of your choice in from of h1 and h2

@app.route("/login/")
def login(): # redirect and url_for we need to redirect the users
    # return "<h1> Welcome to the login page </h1> <h2> Please enter your user login details </h2>"
    return redirect(url_for("welcome")) # this will redirect the users to welcome page

@app.route("/<username>/")
def greet_user(username):
    return f"Welcome to the flask app {username}" # Display the name back to user in browser
if __name__ == "__main__":
    app.run(debug=True)
# Let's add pur html file to redirect from python flask to .html file
#  We need to create a folder called templates
# project folder
#   templates folder
#         welcome.html
#   app.py

# What if the login page is unavailable?
# We would like to redirect the users if they visit login page

