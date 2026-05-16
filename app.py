from flask import Flask, render_template, request, redirect, session
import pickle
import re
import numpy as np
import json
import os

app = Flask(__name__)
app.secret_key = "secret123"

# LOAD MODEL
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# FILES
USER_FILE = "users.json"

# CREATE USERS FILE IF NOT EXISTS
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

# TEXT CLEANING
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(data):
    with open(USER_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    message = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_users()

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/home")
        else:
            message = "❌ Invalid username or password"

    return render_template("login.html", message=message)

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    message = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_users()

        if username in users:
            message = "⚠️ User already exists"
        else:
            users[username] = password
            save_users(users)
            message = "✅ Registered successfully! Go to login."

    return render_template("register.html", message=message)

# ---------------- HOME ----------------
@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/")

    result = None

    if request.method == "POST":
        message = request.form["message"]

        cleaned = preprocess(message)
        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]
        probabilities = model.predict_proba(vector)[0]
        confidence = np.max(probabilities) * 100

        if prediction == "spam":
            result = f"🚨 SPAM DETECTED ({confidence:.2f}%)"
        else:
            result = f"✅ NOT SPAM ({confidence:.2f}%)"

    return render_template("home.html", result=result)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)