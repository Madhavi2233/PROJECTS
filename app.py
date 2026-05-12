from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def home():
    qr_path = None

    if request.method == "POST":
        data = request.form["data"]

        img = qrcode.make(data)

        qr_path = "static/my_qr.png"

        img.save(qr_path)

    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(debug=True)