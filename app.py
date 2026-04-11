import random
from flask import Flask, request
app = Flask(__name__)

secret_number = random.randint(1,100)

@app.route("/")
def home():
    return """
    <h1>Угадай число от 1 до 100</h1>
    <form action="/guess" method="post">
        <input type="number" name="guess" min="1" max="100">
        <button type="submit">Угадать</button>
    </form>
    """

@app.route("/health")
def health():
    return {"status":"healthy"}

@app.route("/guess", methods=["POST"])
def guess():
    number = int(request.form["guess"])
    if number > secret_number:
        return "Bolshe"
    elif number < secret_number:
        return "Menshe"
    else:
        return "Ugadal"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)