import random
from flask import Flask, request, redirect
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
    guess_value = request.form["guess"]
    if not guess_value:
        return redirect("/")
    number = int(guess_value)
    if number > secret_number:
        result = "Меньше! Попробуй меньше."
    elif number < secret_number:
        result = "Больше! Попробуй больше."
    else:
        result = "Угадал! 🎉"
    
    return f"""
    <h1>Угадай число от 1 до 100</h1>
    <p>{result}</p>
    <form action="/guess" method="post">
        <input type="number" name="guess" min="1" max="100">
        <button type="submit">Угадать</button>
    </form>
    <a href="/restart"><button>Новая игра</button></a>
    """
@app.route("/restart")
def restart():
    global secret_number
    secret_number = random.randint(1,100)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
