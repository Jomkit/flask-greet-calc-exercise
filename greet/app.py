from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Home Page for Greet App"""
    html = """
    <h1>Home Page for Welcome App</h1>
    <a href="/welcome">Go To Welcome Page</a>
    <br>
    <a href="/welcome/home">Go To Welcome Home Page</a>
    <br>
    <a href="/welcome/back">Go To Welcome Back Page</a>
    
    """
    return html

@app.route('/welcome')
def welcome():
    """Page that says 'welcome' """
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """Page that says 'welcome home' """
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Page that says 'welcome back' """
    return "welcome back"
    