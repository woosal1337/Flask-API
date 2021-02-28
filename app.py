from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "hello": "world"
    }



# ?argument
@app.route("/hello/")
def hello():
    name = request.args.get("name")
    return jsonify(data=name), 200


if __name__ == "__main__":
    app.run()
