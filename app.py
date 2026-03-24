from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")

        flowers = {
            "rose": request.form.get("rose") or 0,
            "tulip": request.form.get("tulip") or 0,
            "lily": request.form.get("lily") or 0,
            "sunflower": request.form.get("sunflower") or 0
        }

        return render_template("bouquet.html", name=name, flowers=flowers)

    return render_template("index.html")

app.run(debug=True)