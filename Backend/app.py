
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def etusivu():
    return "Backend toimii!"

@app.route("/api/test")
def test():
    return jsonify({
        "viesti": "Flask-backend toimii!"
    })

if __name__ == "__main__":
    app.run(debug=True)
