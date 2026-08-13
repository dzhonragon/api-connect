from flask import Flask, jsonify
from routes.users import users_bp

app = Flask(__name__)

app.register_blueprint(users_bp)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "data": {
            "mensagem": "API Connect esta funcionando!"
        }
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
