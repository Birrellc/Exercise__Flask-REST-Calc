# Import required modules
from flask import Flask, make_response

# instantiate Flask application.
app = Flask(__name__)

# returns the sum of path parameters x and y


@app.route('/calc/web/add/<x>/to/<y>', methods=['GET'])
def add(x, y):
    return make_response(str(int(x) + int(y)), 200)

# returns the difference of path parameters x and y


@app.route('/calc/web/subtract/<x>/from/<y>', methods=['GET'])
def subtract(x, y):
    return make_response(str(int(y) - int(x)), 200)

# returns the product of path parameters x and y


@app.route('/calc/web/multiply/<x>/by/<y>', methods=['GET'])
def multiply(x, y):
    return make_response(str(int(x) * int(y)), 200)

# returns the quotient of path parameters x and y and returns error if y is 0


@app.route('/calc/web/divide/<x>/by/<y>', methods=['GET'])
def divide(x, y):
    return make_response(str(int(x) / int(y)), 200)
