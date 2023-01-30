from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fun/<int:n>')
def func(n):
    ans={
        "number":n,
        "result":n*n

    }
    return jsonify(ans)
app.run(debug=True)