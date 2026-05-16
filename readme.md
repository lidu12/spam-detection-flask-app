

# 📩 Spam Detection Web App (Flask + Machine Learning)

## 🚀 Project Overview

This is a full-stack web application that detects whether a given SMS/message is **Spam or Not Spam** using a Machine Learning model.
The backend is built with **Flask**, and the ML model uses **Naive Bayes + CountVectorizer** trained on a real SMS dataset.

---

## 🧠 Features

* 📊 Machine Learning spam classification
* 🌐 Web interface using Flask
* ✍️ User can input any message
* ⚡ Instant prediction (Spam / Not Spam)
* 🎯 Clean and simple UI
* 💾 Trained model saved using Pickle

---

## 🛠️ Tech Stack

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas 📊
* HTML / CSS 🎨
* Machine Learning (Naive Bayes)

---

## 📁 Project Structure
spam-flask-app/
│
├── train.py              # Model training script
├── app.py                # Flask backend
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # Text vectorizer
│
├── templates/
│     └── index.html     # Frontend UI
│
└── static/
      └── style.css      # Styling


## ⚙️ How It Works

1. User enters a message on the website
2. Flask backend receives input
3. Text is cleaned (preprocessing)
4. Message is converted into numbers (CountVectorizer)
5. ML model predicts Spam or Not Spam
6. Result is displayed on the web page


## ▶️ How to Run Locally

### 1. Clone repository


git clone https://github.com/lidu12/spam-detection-flask-app.git


### 2. Install dependencies


pip install pandas scikit-learn flask


### 3. Train the model


python train.py


### 4. Run the web app


python app.py


### 5. Open in browser


http://127.0.0.1:5000


## 🎯 Learning Outcomes

* Machine Learning model training
* Text preprocessing (NLP basics)
* Web development using Flask
* Model deployment in web application
* End-to-end AI project development

---

## 🔥 Future Improvements

* Deploy on cloud (Render / Railway) ☁️
* Add confidence score (%)
* Improve UI design
* Add live prediction (no refresh)
* Add login system

---

## 👩‍💻 Author

**Lidiya Aramde**
GitHub: [https://github.com/lidu12](https://github.com/lidu12)
3rd Year Computer Science Student
Interests: Cloud Computing ☁️ | Cybersecurity 🔐 | AI/ML 🤖

---

## ⭐ Note

This project was built as part of my learning journey in Machine Learning and Web Development.

---

# 🚀 Done

