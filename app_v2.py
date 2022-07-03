# Import required modules
from flask import Flask, request, make_response, jsonify
import math
import statistics
import operator
from decimal import Decimal

# instantiate Flask application.
app = Flask(__name__)


# helper function to change decimal to full value numbers eg: 3.0 to 3


def decimal_or_integer(x):
    value = math.ceil(x) - math.floor(x)
    if value == 0:
        return math.floor(x)
    return x

# error handler function


def error_handler(message, error_code):
    return jsonify({
        "Error": {
            "Message": message,
            "Success": False,
        }
    }), error_code

# success handler function


def success_hander(equation, ans, success_code):
    return jsonify({
        "Calculation": {
            "Message": "Successful result",
            "Success": True,
            "Text": equation,
            "Result": ans
        }}), success_code


# object allowing access of different operators for routes

ops = {
    "add": operator.add,
    "subtract": operator.sub,
    "multiply": operator.mul,
    "divide": operator.truediv
}


@app.route('/calc/<request_type>/<operation>/<x>/<y>', methods=['GET', 'POST'])
def add(request_type, operation, x=None, y=None):
    try:
        ans = decimal_or_integer(ops[operation](Decimal(y), Decimal(x)))
        if operation == "subtract":
            equation = f' {str(y)} - {str(x)} = {str(ans)}'
        else:
            equation = f'{operation} {str(x)} and {str(y)} = {str(ans)}'

        if request.method == 'GET' and request_type == 'web':
            response = equation
            return make_response(response, 200)

        if request.method == 'GET' and request_type == 'api':
            return success_hander(equation, ans, 200)

    except ZeroDivisionError:
        # return Cannot divide by zero error
        return error_handler('Cannot divide by Zero', 400)


@app.route('/calc/<request_type>/sum', methods=['GET', 'POST'])
def calculate_sum(request_type,):
    ans = decimal_or_integer(
        sum(map(Decimal, request.args.getlist('numbers'))))
    equation = '+'.join(request.args.getlist('numbers')
                        ) + ' = ' + str(ans)

    if request.method == 'GET' and request_type == 'web':
        response = equation
        print(response)
        return make_response(response, 200)

    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    elif request.method == 'POST' and request_type == 'api':
        if 'Numbers' in request.json:
            numbers = request.json['Numbers']

        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        convstr = [str(i) for i in numbers]
        ans = decimal_or_integer(sum(map(Decimal, numbers)))
        equation = ' + '.join(convstr) + ' = '

        return success_hander(equation, ans, 200)
    else:
        return error_handler('Invalid Method', 400)


@app.route('/calc/<request_type>/product', methods=['GET', 'POST'])
def calculate_product(request_type):
    ans = decimal_or_integer(
        math.prod(map(Decimal, request.args.getlist('numbers'))))
    equation = ' x ' .join(request.args.getlist(
        'numbers')) + ' = '

    if request.method == 'GET' and request_type == 'web':
        response = equation
        return make_response(response, 200)

    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    elif request.method == 'POST' and request_type == 'api':
        if 'Numbers' in request.json:
            numbers = request.json['Numbers']

        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        print(numbers)
        ans = decimal_or_integer(math.prod(map(Decimal, numbers)))
        convstr = [str(i) for i in numbers]
        equation = ' x '.join(convstr) + ' = '

        return success_hander(equation, ans, 200)

    else:
        return error_handler('Invalid Method', 400)


@app.route('/calc/<request_type>/mean', methods=['GET', 'POST'])
def calculate_average(request_type):
    ans = decimal_or_integer(
        statistics.mean(map(Decimal, request.args.getlist('numbers'))))
    equation = '(' + ' + ' .join(request.args.getlist(
        'numbers')) + ') / ' + str(len(request.args.getlist('numbers'))) + ' = '

    if request.method == 'GET' and request_type == 'web':
        response = equation
        return make_response(response, 200)

    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    elif request.method == 'POST' and request_type == 'api':

        if 'Numbers' in request.json:
            numbers = request.json['Numbers']

        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        ans = decimal_or_integer(
            statistics.mean(map(Decimal, numbers)))
        convstr = [str(i) for i in numbers]
        equation = '(' + ' + '.join(convstr) + ') / ' + \
            str(len(convstr)) + ' = '

        return success_hander(equation, ans, 200)

    else:
        return error_handler('Invalid Method', 400)
