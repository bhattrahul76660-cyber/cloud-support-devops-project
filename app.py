from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Customer Support Ticket API",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/tickets")
def tickets():
    return jsonify({
        "tickets": [
            {
                "id": 101,
                "issue": "Login problem",
                "status": "open"
            },
            {
                "id": 102,
                "issue": "Password reset",
                "status": "resolved"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)