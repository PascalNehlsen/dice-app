import random
from flask import Flask, render_template
from os import environ

app = Flask(__name__)

OWNER = environ.get("OWNER", "Mr. X")
BG_COLOR = environ.get("BG_COLOR", "#0c7077")
DICE_COLOR = environ.get("DICE_COLOR", "#eb856b")

@app.route("/")
def init():
    return render_template('index.html', OWNER=OWNER, BG_COLOR=BG_COLOR, DICE_COLOR=DICE_COLOR)

@app.route("/dice")
def dice():
    result: int = random.randint(1, 6)
    return render_template('dice.html', result=result, OWNER=OWNER, BG_COLOR=BG_COLOR, DICE_COLOR=DICE_COLOR)

@app.route("/proof")
def proof():
    return "proof"

if __name__ == "__main__":
    app.run(debug=True)
