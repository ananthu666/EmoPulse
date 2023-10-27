from flask import Flask, request, render_template
from senti import analyse

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    response = ""

    if request.method == "POST":
        text = request.form.get("text")
        scor, res = analyse(text)
        sentiment = scor
        response = res

    return render_template("index.html", sentiment=sentiment, response=response)

if __name__ == "__main__":
    app.run(debug=True)