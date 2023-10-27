# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def home_page():
    """Home Page for Calculator App"""  
    html = """
    <h1>Calculator App</h1>
    <h3>Built with Flask</h3>
    <p>Perform math operation in url</p>
    <p>Example: "localhost:5000/add?a=2&b=3"</p>
    """
    return html

@app.route('/add')
def addition():
    """Performs addition operation"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.add(a,b)}"

@app.route('/sub')
def subtraction():
    """Performs subtraction operation"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.sub(a,b)}"
    
@app.route('/mult')
def multiplication():
    """Performs multiplication operation"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.mult(a,b)}"

@app.route('/div')
def division():
    """Performs division operation"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{operations.div(a,b)}"

@app.route('/math/<op>')
def math_operation(op):
    """Dynamic routing to handle multiple choices of math operations"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    operation = {
        'add': operations.add,
        'sub': operations.sub, 
        'mult': operations.mult,
        'div': operations.div
        }
    return f"{operation[op](a,b)}"