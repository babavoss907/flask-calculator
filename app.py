from flask import Flask, render_template, request
import json
# from calculate import calculate

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.post('/calculate')
def calculate():
    data = request.json
    result = 0
    current_number = 0
    operator = None
    # import pdb;pdb.set_trace()
    for item in data['numbers']:
        if item in ['+', '-', 'x', '/']:
            operator = item
            if operator is None:
                result = current_number
            else:
                if operator == '+':
                    result += current_number
                elif operator == '-':
                    result -= current_number
                elif operator == 'x':
                    result *= current_number
                elif operator == '/':
                    result /= current_number
            operator = item
            current_number = 0
        else:
            current_number = current_number*10 + int(item)
            result = current_number
        if operator is None:
            result = current_number
        else:
            if operator == '+':
                result += current_number
            elif operator == '-':
                result -= current_number
            elif operator == 'x':
                result *= current_number
            elif operator == '/':
                result /= current_number
    return json.dumps({'result': result})

if __name__ == '__main__':
    app.run(debug=True)