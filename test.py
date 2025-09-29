from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask 2.3.2!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", por
