# Aura: Multilingual Social Sentiment Analyzer 🌟

Aura is a dual-component project consisting of a Google Chrome Extension (Frontend UI) and a Python Flask API (Backend) powered by Natural Language Processing (NLP). It evaluates the overall emotional impact of text and social media links across platforms like YouTube, Reddit, and X using a calm, smooth visual dashboard.

## ✨ Key Features
- **Multilingual Support:** Automatically detects and translates non-English comments (Hindi, Spanish, French, etc.) before running sentiment analysis.
- **Dual Modes:** Paste direct social media thread links or manually paste specific paragraphs/comments.
- **Calm UI:** Features a glassmorphic design with smooth CSS-animated bar graphs representing Positive, Neutral, and Negative impact.

## 🚀 Getting Started

### 1. Backend Setup (Python)
Navigate to the backend directory, install the dependencies, and run the server:
```bash
cd aura-backend
pip install -r requirements.txt
python app.py