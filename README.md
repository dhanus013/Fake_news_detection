

# 📰 Fake News Detector

A simple **Fake News Detection Web App** built using **Flask**, **TF-IDF Vectorization**, and **Logistic Regression**.
Users can enter any news text, and the model will classify it as **Fake** or **Real** with a confidence score.

---

## ✨ Features

✅ Enter any news text and check if it’s Fake or Real
✅ ML Model trained using **TF-IDF + Logistic Regression**
✅ Displays prediction with confidence percentage
✅ Web-based UI built with **Flask & HTML/CSS**
✅ Confidence thresholding (uncertain predictions are highlighted)

---

## 🚀 Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **ML Model:** TF-IDF + Logistic Regression (scikit-learn)
* **Other Libraries:** NLTK / Regex for text cleaning, Pickle for model storage

---

## 📂 Project Structure

```
fake-news-detector/
│── static/               # CSS / Images
│── templates/            # HTML Templates
│   └── index.html
│── model.pkl             # Trained Logistic Regression model
│── vectorizer.pkl        # TF-IDF vectorizer
│── app.py                # Flask backend
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
```

---

## ⚡ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

### 2️⃣ Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Now open **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** in your browser 🎉

---

## 🎯 Usage

1. Enter a news headline or paragraph
2. Click **Check**
3. Get prediction → **Fake** 🟥 or **Real** 🟩 with confidence score

---

## 📸 Screenshots

🔹 **Home Page**
<img width="1366" height="768" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/67a73b3b-2768-4449-a04a-37cb4e0d9855" />


🔹 **Prediction Result**

<img width="1366" height="768" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/117bff99-3774-4e81-b594-250c5074d646" />


## 📊 Model Details

* **Vectorizer:** TF-IDF
* **Algorithm:** Logistic Regression
* **Training Dataset:** Kaggle Fake News Dataset (or your dataset)
* **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score



## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.





