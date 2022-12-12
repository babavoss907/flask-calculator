import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/calculator')
def calculator():
    return render_template('calculator.html')

@app.post('/calculate')
def calculate():
    if request.method == 'POST':
        data = request.get_json()
        return json.dumps({'result': data})

if __name__ == '__main__':
    app.run(debug=True)