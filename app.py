  from flask import Flask, render_template, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
@app.route('/')
def index():
    return render_template('index.html',num1=1, num2=2, addition=add(1,2),\
            subtract=subtract(1,2),multiply=multiply(1,2))

@app.route('/io', methods=['GET'])
def return_json():

    return jsonify({'tasks': tasks})


def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
