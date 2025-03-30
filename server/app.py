#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route ('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route ('/print/<string:str>')
def print_string(str):
    print (f'{str}')
    return f'{str}'

@app.route ('/count/<int:integer>')
def count(integer):
    numbers = ""
    for i in range(0, integer):
        numbers += f'{i}\n'
    return numbers

@app.route ('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        sum = num1 + num2
        return f'{sum}'
    elif operation == '-':
        sub = num1 - num2
        return f'{sub}'
    elif operation == '*':
        multi = num1 * num2
        return f'{multi}'
    elif operation == 'div':
        div = num1 / num2
        return f'{div}'
    elif operation == '%':
        modulo = num1 % num2
        return f'{modulo}'
    else:
        return None
    