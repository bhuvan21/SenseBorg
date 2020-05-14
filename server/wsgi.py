from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    content = request.args.get("main")
    print(content)
    return 'Hello, World!'

app.run(host='0.0.0.0', ssl_context=("B:\etc\letsencrypt\live\senseborg.ddns.net\winfullchain.pem", "B:\etc\letsencrypt\live\senseborg.ddns.net\winprivkey.pem"))