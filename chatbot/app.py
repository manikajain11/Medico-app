from distutils.log import debug
from email import message
from urllib import response
from flask import Flask, jsonify, render_template, request
from infer import get_response

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug = True)
