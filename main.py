from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]  # The name property in the input tag
        last_name = request.form["last_name"]
        email = request.form["email"]
        available = request.form["available"]
        occupation = request.form["occupation"]

    return render_template("index.html")


app.run(debug=True, port=5001)
