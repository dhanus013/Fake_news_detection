from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

import joblib

# Load models
vectorizer = joblib.load("tfidf_vectorizer.pkl")
model = joblib.load("logistic_model.pkl")

def clean_text(text):
    return text.lower().strip()


def predict_news(text, threshold=60):
    clean = clean_text(text)
    vectorized = vectorizer.transform([clean])
    prediction = model.predict(vectorized)[0]
    prob = model.predict_proba(vectorized)[0]
    confidence = round(prob[prediction] * 100, 2)
    label = "Real" if prediction == 1 else "Fake"
    if confidence < threshold:
        label = f"{label} (Uncertain)"
    return label, confidence


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        news_text = request.form["news"]
        label, confidence = predict_news(news_text)
        result = f"Prediction: {label} | Confidence: {confidence}%"
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
