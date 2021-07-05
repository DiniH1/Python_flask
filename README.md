# Model View Controller (MVC) with Python Flask
## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps


### Creating a file called app.py
#### Let's see how we can use Python Flask to interact with our browser

`from flask import Flask`
- We have to create an object of this class

`app = Flask(__name__)` 
- creating an app instance

### Let's create a function to link to our home//default page
#### Let's connect this function to our browser
```
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

`if __name__ == "__main__":
    app.run(debug=True)`
- Let's add pur html file to redirect from python flask to .html file
- We need to create a folder called templates
```
project folder
   templates folder
         welcome.html
   app.py
```
### What if the login page is unavailable?
- We would like to redirect the users if they visit login page
