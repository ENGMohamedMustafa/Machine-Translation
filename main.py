from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator  # Using Google Translate API

app = Flask(__name__)
CORS(app)  # To allow cross-origin requests (needed for frontend and backend interaction)

translator = Translator()

# Route to handle translation requests
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    target_lang = data.get('target_lang', 'en')
    
    if not text:
        return jsonify({'error': 'Text is required for translation'}), 400

    try:
        # Translating the text to the target language
        translated = translator.translate(text, dest=target_lang)
        return jsonify({'translated_text': translated.text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
