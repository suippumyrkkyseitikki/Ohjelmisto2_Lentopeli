from database import luo_yhteys
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/")
def etusivu():
    return "Backend toimii!"

@app.route("/api/test")
def test():
    return jsonify({
        "viesti": "Flask-backend toimii!"
    })



@app.route("/api/tietokantatesti")
def tietokantatesti():
    try:
        yhteys = luo_yhteys()
        yhteys.close()

        return {
            "viesti": "Tietokantayhteys toimii!"
        }

    except mysql.connector.Error as virhe:
        return {
            "virhe": str(virhe)
        }, 500

if __name__ == "__main__":
        app.run(debug=True)