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
DATA_FILE = "data.json"

# CREATE FILES IF NOT EXIST
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

# CLEAN TEXT
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# LOAD JSON
def load_json(file):
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_json(USER_FILE)

        if username in users and users[username] == password:
            session["user"] = username
            return redirect("/home")

    return render_template("login.html")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_json(USER_FILE)
        users[username] = password
        save_json(USER_FILE, users)

        return redirect("/")

    return render_template("register.html")

# HOME (MAIN APP)
@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect("/")

    result = None
    history = []

    data = load_json(DATA_FILE)
    user = session["user"]

    if user not in data:
        data[user] = []

    if request.method == "POST":
        message = request.form["message"]

        cleaned = preprocess(message)
        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]
        probabilities = model.predict_proba(vector)[0]
        confidence = np.max(probabilities) * 100

        if prediction == "spam":
            result = f"🚨 SPAM ({confidence:.2f}%)"
        else:
            result = f"✅ NOT SPAM ({confidence:.2f}%)"

        # SAVE HISTORY
        data[user].append({
            "message": message,
            "result": result
        })

        save_json(DATA_FILE, data)

    history = data[user]

    return render_template("home.html", result=result, history=history)

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)