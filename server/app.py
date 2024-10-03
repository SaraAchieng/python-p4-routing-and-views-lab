#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    print(name)
    
    return name

@app.route('/count/<int:param>')
def count(param):
    # Generate the range of numbers and join them with '\n' for plain text
    numbers = '<br>'.join(str(i) for i in range(1, param))
    
    # Return the numbers as plain text
    return numbers, 200, {'Content-Type': 'text/plain'}


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'



    
    



if __name__ == '__main__':
    app.run(port=5555, debug=True)
