from flask import Flask, make_response, request, jsonify
from decimal import Decimal
import math
import statistics


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

# returns the sum of path parameters x and y


@app.route('/calc/<request_type>/add/<x>/to/<y>', methods=['GET'])
def add(x, y, request_type):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(Decimal(x) + Decimal(y))
    equation = f'{str(x)} + {str(y)} = {str(ans)}'

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        return make_response(equation, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

# returns the difference of path parameters x and y


@app.route('/calc/<request_type>/subtract/<x>/from/<y>', methods=['GET'])
def subtract(x, y, request_type):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(Decimal(y) - Decimal(x))
    equation = f'{(y)} - {(x)} = {(ans)}'

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        return make_response(equation, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)


# returns the product of path parameters x and y


@app.route('/calc/<request_type>/multiply/<x>/by/<y>', methods=['GET'])
def multiply(x, y, request_type):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(Decimal(x) * Decimal(y))
    equation = f'{str(x)} * {str(y)} = {str(ans)}'

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        return make_response(equation, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

# returns the division of path parameters x and y


@app.route('/calc/<request_type>/divide/<x>/by/<y>', methods=['GET'])
def divide(x, y, request_type):
    try:
        # performs the required calculation with the provided operation
        ans = decimal_or_integer(Decimal(x) / Decimal(y))
        equation = f'{str(x)} / {str(y)} = {str(ans)}'

        # returns the calculation result in a string format
        if request.method == 'GET' and request_type == 'web':
            return make_response(equation, 200)

        # returns the calculation result in a JSON format
        if request.method == 'GET' and request_type == 'api':
            return success_hander(equation, ans, 200)

    except ZeroDivisionError:
        # return Cannot divide by zero error
        return error_handler('Cannot divide by 0', 400)


@app.route('/calc/<request_type>/sum', methods=['GET', 'POST'])
def calculate_sum(request_type,):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(
        sum(map(Decimal, request.args.getlist('numbers'))))
    equation = '+'.join(request.args.getlist('numbers')
                        ) + ' = ' + str(ans)

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        response = equation
        return make_response(response, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    # using POST to send the JSON payload to the endpoint
    elif request.method == 'POST' and request_type == 'api':
        if 'Numbers' in request.json:
            numbers = request.json['Numbers']

        # if paramaters in url and no Numbers property in JSON body use the paramaters
        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        # for all i in array convert to string (so we can use the .join method for the equation below)
        convstr = [str(i) for i in numbers]
        equation = ' + '.join(convstr) + ' = '
        ans = decimal_or_integer(sum(map(Decimal, numbers)))

        return success_hander(equation, ans, 200)
    else:
        return error_handler('Invalid Method', 400)


@app.route('/calc/<request_type>/product', methods=['GET', 'POST'])
def calculate_product(request_type):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(
        math.prod(map(Decimal, request.args.getlist('numbers'))))
    equation = ' x ' .join(request.args.getlist(
        'numbers')) + ' = '

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        response = equation
        return make_response(response, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    # using POST to send the JSON payload to the endpoint
    elif request.method == 'POST' and request_type == 'api':
        if 'Numbers' in request.json:
            numbers = request.json['Numbers']

        # if paramaters in url and no Numbers property in JSON body use the paramaters
        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        print(numbers)

        # for all i in array convert to string (so we can use the .join method for the equation below)
        convstr = [str(i) for i in numbers]
        equation = ' x '.join(convstr) + ' = '
        ans = decimal_or_integer(math.prod(map(Decimal, numbers)))

        return success_hander(equation, ans, 200)
    else:
        return error_handler('Invalid Method', 400)


@app.route('/calc/<request_type>/mean', methods=['GET', 'POST'])
def calculate_average(request_type):
    # performs the required calculation with the provided operation
    ans = decimal_or_integer(
        statistics.mean(map(Decimal, request.args.getlist('numbers'))))

    equation = '(' + ' + ' .join(request.args.getlist(
        'numbers')) + ') / ' + str(len(request.args.getlist('numbers'))) + ' = '

    # returns the calculation result in a string format
    if request.method == 'GET' and request_type == 'web':
        response = equation
        return make_response(response, 200)

    # returns the calculation result in a JSON format
    if request.method == 'GET' and request_type == 'api':
        return success_hander(equation, ans, 200)

    # using POST to send the JSON payload to the endpoint
    elif request.method == 'POST' and request_type == 'api':
        if 'Numbers' in request.json:
            numbers = request.json['Numbers']
        # if paramaters in url and no Numbers property in JSON body use the paramaters
        elif len(request.args.getlist('numbers')) > 0 and 'Numbers' not in request.json:
            numbers = request.args.getlist('numbers')

        else:
            return error_handler('Incorrect JSON data found', 400)

        if len(numbers) == 0:
            return error_handler('Empty List', 400)

        # for all i in array convert to string (so we can use the .join method for the equation below)
        convstr = [str(i) for i in numbers]
        equation = '(' + ' + '.join(convstr) + ') / ' + \
            str(len(convstr)) + ' = '
        ans = decimal_or_integer(
            statistics.mean(map(Decimal, numbers)))

        return success_hander(equation, ans, 200)

    else:
        return error_handler('Invalid Method', 400)
