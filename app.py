# Import required modules
from flask import Flask, make_response, request
from decimal import Decimal
import math
import statistics

# instantiate Flask application.
app = Flask(__name__)


# helper function to change decimal to full value numbers eg: 3.0 to 3

def decimal_or_integer(x):
    value = math.ceil(x) - math.floor(x)
    if value == 0:
        return math.floor(x)
    return x

# returns the sum of path parameters x and y


@app.route('/calc/web/add/<x>/to/<y>', methods=['GET'])
def add(x, y):
    ans = decimal_or_integer(Decimal(x) + Decimal(y))
    equation = f'{str(x)} + {str(y)} = {str(ans)}'
    return make_response(equation, 200)

# returns the difference of path parameters x and y


@app.route('/calc/web/subtract/<x>/from/<y>', methods=['GET'])
def subtract(x, y):
    ans = decimal_or_integer(Decimal(y) - Decimal(x))
    equation = f'{(y)} - {(x)} = {(ans)}'
    return make_response(equation, 200)

# returns the product of path parameters x and y


@app.route('/calc/web/multiply/<x>/by/<y>', methods=['GET'])
def multiply(x, y):
    ans = decimal_or_integer(Decimal(x) * Decimal(y))
    equation = f'{str(x)} * {str(y)} = {str(ans)}'
    return make_response(equation, 200)

# returns the quotient of path parameters x and y and returns error if y is 0


@app.route('/calc/web/divide/<x>/by/<y>', methods=['GET'])
def divide(x, y):
    try:
        ans = decimal_or_integer(Decimal(x) / Decimal(y))
        equation = f'{str(x)} / {str(y)} = {str(ans)}'
        return make_response(equation, 200)
    except ZeroDivisionError:
        # return Cannot divide by zero error
        return make_response("Cannot divide by zero", 400)


@app.route('/calc/web/sum', methods=['GET'])
def calculate_sum():
    try:
        ans = decimal_or_integer(
            sum(map(Decimal, request.args.getlist('numbers'))))
        equation = '+'.join(request.args.getlist('numbers')
                            ) + ' = ' + str(ans)
        return make_response(equation, 200)
    except ValueError:
        # Make a response to Invalid input such as a string instead of an integer is present in the query parameter
        return make_response("Invalid input", 400)


@ app.route('/calc/web/product', methods=['GET'])
def calculate_product():
    try:
        ans = decimal_or_integer(
            math.prod(map(Decimal, request.args.getlist('numbers'))))
        equation = ' x ' .join(request.args.getlist(
            'numbers')) + ' = ' + str(ans)
        return make_response(equation, 200)
    except ValueError:
        return make_response("Invalid input", 400)


@ app.route('/calc/web/mean', methods=['GET'])
def calculate_mean():
    try:
        ans = decimal_or_integer(statistics.mean(
            map(Decimal, request.args.getlist('numbers'))))
        equation = '(' + ' + '.join(request.args.getlist(
            'numbers')) + ') / ' + str(len(request.args.getlist('numbers'))) + ' = ' + str(ans)
        return make_response(equation, 200)
    except ValueError:
        return make_response("Invalid input", 400)
