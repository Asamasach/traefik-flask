from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route("/")
def user_service_hello():
    return make_response(jsonify(
        {
            "msg": "Hello my friend :)"
        }
    ), 200)
