import numpy as np
from flask import Flask, request, jsonify, render_template
from chat import get_response

#Create the flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/get")
def chat():
    data = request.get_json()
    message = data['message']
    response = get_response(message)
    return jsonify({'response':response})


if __name__ == '__main__':
    flask_app.run(port=5000)

