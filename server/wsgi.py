from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    content = request.args.get("test")
    print(content)
    return 'Hello, World!'

app.run(host='0.0.0.0')