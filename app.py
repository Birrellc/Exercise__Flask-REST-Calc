# Import required modules
from flask import Flask, make_response, request
from decimal import Decimal
import math
import statistics

# instantiate Flask application.
app = Flask(__name__)

# returns the sum of path parameters x and y


@app.route('/calc/web/add/<x>/to/<y>', methods=['GET'])
def add(x, y):
    ans = (Decimal(x) + Decimal(y))
    equation = f'{str(x)} + {str(y)} = {str(ans)}'
    return make_response(equation, 200)

# returns the difference of path parameters x and y


@app.route('/calc/web/subtract/<x>/from/<y>', methods=['GET'])
def subtract(x, y):
    ans = (Decimal(x) - Decimal(y))
    equation = f'{str(x)} - {str(y)} = {str(ans)}'
    return make_response(equation, 200)

# returns the product of path parameters x and y


@app.route('/calc/web/multiply/<x>/by/<y>', methods=['GET'])
def multiply(x, y):
    ans = (Decimal(x) * Decimal(y))
    equation = f'{str(x)} * {str(y)} = {str(ans)}'
    return make_response(equation, 200)

# returns the quotient of path parameters x and y and returns error if y is 0


@app.route('/calc/web/divide/<x>/by/<y>', methods=['GET'])
def divide(x, y):
    ans = (Decimal(x) / Decimal(y))
    equation = f'{str(x)} / {str(y)} = {str(ans)}'
    try:
        return make_response(equation, 200)
    except ZeroDivisionError:
        # return Cannot divide by zero error
        return make_response("Cannot divide by zero", 400)
