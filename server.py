from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'


@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    n1 = data.get("first", 0)
    n2 = data.get("second", 0)
    result = n1 + n2
    return f'result: {result}'


@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    n1 = data.get("first", 0)
    n2 = data.get("second", 0)
    result = n1 - n2
    return f'result: {result}'


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
