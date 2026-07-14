from flask import Flask, render_template, request
from medical_ai import ask_medical_ai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        symptoms = request.form["symptoms"]

        answer = ask_medical_ai(symptoms)

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)