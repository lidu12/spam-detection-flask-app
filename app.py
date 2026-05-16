from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# LOAD MODEL
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# CLEAN TEXT
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        message = request.form["message"]
        cleaned = preprocess(message)

        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == "spam":
            result = "🚨 SPAM DETECTED"
        else:
            result = "✅ NOT SPAM"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)