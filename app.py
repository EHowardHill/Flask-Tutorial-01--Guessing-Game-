from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/guess", methods=["POST"])
def guess():

    guessed_number = request.json.get("guessed_number")
    guessed_number = int(guessed_number)

    with open("number.txt", "r") as f:
        data = f.read()
        real_number = int(data)

    print([guessed_number, real_number])

    if guessed_number < real_number:
        return {"answer": "too low"}

    elif guessed_number > real_number:
        return {"answer": "too high"}

    return {"answer": "just right"}


@app.route("/")
def hello_world():

    with open("number.txt", "w") as f:
        number = random.randint(0, 100)
        data = str(number)
        f.write(data)

    return render_template("index.html")
