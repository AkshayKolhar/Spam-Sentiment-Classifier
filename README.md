# 📧 Spam & Sentiment Classifier

An end-to-end **Machine Learning and NLP web application** that classifies text messages as **Spam or Not Spam** and performs **Sentiment Analysis**.

🌐 **Live Demo:** [Spam & Sentiment Classifier](https://spam-sentiment-classifier.onrender.com/)

---

## 🚀 Project Overview

The **Spam & Sentiment Classifier** is an end-to-end Machine Learning project built using **Python, Scikit-learn, and Flask**.

The application performs two Natural Language Processing (NLP) tasks:

1. **Spam Detection** – Identifies whether a message is Spam or Not Spam.
2. **Sentiment Analysis** – Determines the sentiment expressed in the text and displays the prediction probability.

The trained machine learning models are integrated into a Flask web application and deployed online using **Render**.

---

## ✨ Features

- 📩 Detects Spam messages
- ✅ Identifies legitimate messages
- 😊 Performs Sentiment Analysis
- 📊 Displays sentiment prediction probability
- 🌐 Interactive web interface
- 🤖 Machine Learning-based predictions
- 🚀 Deployed as a live web application

---

## 🌐 Live Demo

🚀 **Try the project here:**

👉 [https://spam-sentiment-classifier.onrender.com/](https://spam-sentiment-classifier.onrender.com/)

---

## 🛠️ Technologies Used

### Programming & Machine Learning

- Python
- Scikit-learn
- Pandas
- NumPy

### NLP Techniques

- TF-IDF Vectorization
- N-grams
- Text Classification

### Machine Learning Models

- LinearSVC
- Logistic Regression

### Web Development

- Flask
- HTML
- CSS
- JavaScript

### Deployment & Version Control

- Git
- GitHub
- Render
- Gunicorn

---

## 🧠 Machine Learning Models

### 📌 Spam Classification

The Spam Detection model uses:

- **TF-IDF Vectorizer**
- **N-grams (1, 2)**
- **Maximum Features: 5000**
- **LinearSVC**

The model predicts whether the input message is:

- Spam
- Not Spam

---

### 📌 Sentiment Classification

The Sentiment Analysis model uses:

- **TF-IDF Vectorizer**
- **Maximum Features: 10000**
- **Logistic Regression**
- **Maximum Iterations: 1000**

The model predicts the sentiment of the given text and provides the probability associated with the predicted sentiment.

---

## 📊 Model Evaluation

The Spam Classification model achieved approximately:

### Accuracy

**97.97%**

### Confusion Matrix

```text
[[901, 2],
 [19, 112]]
```

This demonstrates strong performance in distinguishing spam messages from legitimate messages.

---

## 📂 Project Structure

```text
Spam-Sentiment-classifier/
│
├── data/
│   └── Dataset files
│
├── model/
│   ├── sentiment_prep.pkl
│   └── spam_pred.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── classify.py
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Application Workflow

```text
User Input
    ↓
Spam Classification Model
    ↓
Spam / Not Spam Prediction
    ↓
Sentiment Classification Model
    ↓
Sentiment Prediction
    ↓
Sentiment Probability
    ↓
Results Displayed on Web Interface
```

---

## 🧪 Example Inputs

### Example 1

```text
Congratulations! You won a free iPhone. Click here now!
```

The application analyzes the message and predicts whether it is spam.

### Example 2

```text
This movie was absolutely amazing and I really enjoyed it.
```

The application analyzes the text and predicts its sentiment.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AkshayKolhar/Spam-Sentiment-classifier.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Spam-Sentiment-classifier
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Run the following command:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 📦 Requirements

The project uses the following dependencies:

```text
Flask==3.1.2
gunicorn==23.0.0
scikit-learn==1.7.2
pandas==2.3.2
numpy==2.3.3
```

---

## 🚀 Deployment

The application is deployed using **Render**.

### Deployment Workflow

```text
GitHub Repository
        ↓
Render Web Service
        ↓
Install Dependencies
        ↓
Gunicorn Server
        ↓
Live Web Application
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## 🎯 Key Learnings

Through this project, I gained practical experience in:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Handling duplicate data
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- N-gram features
- Machine Learning Pipelines
- Training classification models
- Model evaluation
- Accuracy calculation
- Confusion Matrix analysis
- Saving trained models using Pickle
- Loading ML models for inference
- Building a Flask web application
- Integrating Machine Learning models with a frontend
- Git and GitHub version control
- Deploying Machine Learning applications using Render
- Using Gunicorn for production deployment

---

## 🔮 Future Improvements

Some possible future improvements include:

- Integrating Transformer-based NLP models
- Adding REST API endpoints
- Adding prediction history
- Improving the user interface
- Adding batch text prediction
- Adding more detailed model evaluation metrics
- Containerizing the application using Docker

---

## 👨‍💻 Author

**Akshay Kolhar**

AI & Machine Learning Engineering Student

GitHub: [AkshayKolhar](https://github.com/AkshayKolhar)

---

## ⭐ Support

If you found this project useful, please consider giving the repository a **star ⭐** on GitHub!

---

### 🚀 Live Application

**[Click here to try the Spam & Sentiment Classifier](https://spam-sentiment-classifier.onrender.com/)**
