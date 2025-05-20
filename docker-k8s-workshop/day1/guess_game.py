from flask import Flask, request, jsonify
import random

app = Flask(__name__)

number = random.randint(1, 10)
attempts = 0

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 10."

@app.route("/guess", methods=["POST"])
def guess():
    global attempts, number
    data = request.json
    if "guess" not in data or not isinstance(data["guess"], int):
        return jsonify({"error": "Please provide a valid number."}), 400

    guess = data["guess"]
    attempts += 1

    if guess == number:
        response = {"message": f"Correct! You guessed it in {attempts} tries."}
        number = random.randint(1, 10)  # Reset the game
        attempts = 0
        return jsonify(response)
    elif guess < number:
        return jsonify({"message": "Too low. Try again."})
    else:
        return jsonify({"message": "Too high. Try again."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
