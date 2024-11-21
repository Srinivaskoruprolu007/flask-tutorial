from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''
# WSGI
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Flask course. Very good course to learn Flask. Go and code Make the ML visible and Interact"
@app.route('/index')
def index():
    return "Welcome to index page"

if __name__ == "__main__":
    app.run(debug=True)
