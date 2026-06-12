# Aura — Sentiment Chrome Extension

Aura is an AI-powered Chrome extension that analyzes text sentiment and identifies emotional tone in real time.

The extension processes user input, sends it through an AI sentiment engine, and displays sentiment insights through a clean and minimal browser experience.

---

# Features

* Real-time sentiment analysis
* Positive / Negative / Neutral detection
* Chrome extension support
* Instant text sentiment evaluation
* Clean and responsive UI
* FastAPI backend
* NLP-powered sentiment engine
* Fast prediction response

---

# Supported Inputs

* Manual Text Input
* Browser Text Selection

Future Support:

* Social Media Integration
* Website-wide Sentiment Detection
* Email Sentiment Analysis
* Multi-language Support

---

# Tech Stack

## Frontend

* HTML
* CSS
* JavaScript
* Chrome Extension API

## Backend

* FastAPI
* Python

## AI / NLP

* HuggingFace Transformers
* Sentiment Classification Model

---

# Project Structure

```bash
Aura-sentiment-extension/
│
├── backend-api/
├── frontend-extension/
├── assets/
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Riktam45/Aura-sentiment-extension.git
```

---

# Backend Setup

```bash
cd backend-api

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Load Chrome Extension

1. Open Chrome

2. Go to:

```text
chrome://extensions/
```

3. Enable Developer Mode

4. Click **Load unpacked**

5. Select:

```text
frontend-extension
```

---

# Future Improvements

* Emotion classification
* Better sentiment accuracy
* Dashboard analytics
* Multi-language support
* Browser-wide analysis
* Cloud synchronization

---

# Author

GitHub: https://github.com/Riktam45
