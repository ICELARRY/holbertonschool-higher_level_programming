#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary to store user data in memory
users = {}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# /data endpoint: returns list of usernames
@app.route("/data")
def data():
    return jsonify(list(users.keys()))

# /status endpoint
@app.route("/status")
def status():
    return "OK"

# /users/<username> endpoint: returns user info or 404 if not found
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint: accepts POST requests to add new users
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Run the Flask app
if __name__ == "__main__":
    print("Server running on port 5000")
    app.run(port=5000)
