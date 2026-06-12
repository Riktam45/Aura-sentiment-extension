from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

# Initialize AI Model Engine
nltk.download('vader_lexicon', quiet=True)
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)
CORS(app) 

def translate_to_english(text):
    """
    Automatically detects the language and translates it to English.
    If it's already English, it returns the original text untouched.
    """
    try:
        # 'auto' tells the engine to automatically discover the source language
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        print(f"Translation notice: {e}")
        return text # Fallback to original text if translation slips

def scrape_and_analyze_url(url):
    print(f"Scraping active link target: {url}")
    # Simulated multilingual distribution for multi-platform threads
    if "reddit" in url.lower():
        return {"positive": 30.0, "neutral": 35.0, "negative": 35.0}
    elif "youtube" in url.lower():
        return {"positive": 70.0, "neutral": 15.0, "negative": 15.0}
    else:
        return {"positive": 50.0, "neutral": 30.0, "negative": 20.0}

@app.route('/analyze', methods=['POST'])
def handle_analysis():
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Missing request body"}), 400
        
    req_type = req_data.get('type')
    payload = req_data.get('data')
    
    if req_type == "text":
        print(f"Original Text received: {payload}")
        
        # Multilingual Translation Layer
        english_text = translate_to_english(payload)
        print(f"Translated to English: {english_text}")
        
        # Analyze using VADER engine
        scores = sia.polarity_scores(english_text)
        
        pos = max(0, scores['pos'] * 100)
        neg = max(0, scores['neg'] * 100)
        neu = max(0, scores['neu'] * 100)
        
        sum_total = pos + neg + neu
        if sum_total > 0:
            pos, neu, neg = (pos/sum_total)*100, (neu/sum_total)*100, (neg/sum_total)*100

        return jsonify({"positive": pos, "neutral": neu, "negative": neg})
        
    elif req_type == "url":
        results = scrape_and_analyze_url(payload)
        return jsonify(results)

    return jsonify({"error": "Invalid request type"}), 400

if __name__ == '__main__':
    # Running on alternative dev port 8080 to prevent server environment clashes
    app.run(host='127.0.0.1', port=8080, debug=True)