from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="Aakash",
    password="ash@123",
    database="mydatabase"
)

cursor = db.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vaccination_status", methods=["POST"])
def vaccination_status():
    reg_no = request.form["reg_no"]
    query = "SELECT Vaccination_Status FROM students WHERE RegNo = %s"
    cursor.execute(query, (reg_no,))
    result = cursor.fetchone()

    if result is None:
        return "No student found with that registration number"
    else:
        return result[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
