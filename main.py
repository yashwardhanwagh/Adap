from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
DATA_FILE = 'data.json'


# Load existing words from JSON file
def load_words():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as data_file:
            try:
                return json.load(data_file)
            except json.JSONDecodeError:
                return {}
    return {}


# Save updated dictionary to JSON
def save_words(word_dict):
    with open(DATA_FILE, 'w') as data_file:
        json.dump(word_dict, data_file, indent=4)


# ➕ Add a new word
@app.route('/add', methods=['POST'])
def add_word():
    word_dict = load_words()
    data = request.get_json()

    word = data.get('word')
    meaning = data.get('meaning')

    if not word or not meaning:
        return jsonify({"error": "Both 'word' and 'meaning' are required"}), 400

    word_dict[word] = meaning
    save_words(word_dict)

    return jsonify({"message": f"'{word}' added successfully!"})


# 🔍 Search for a word
@app.route('/search', methods=['GET'])
def search_word():
    word_dict = load_words()
    word_to_search = request.args.get('word')

    if not word_to_search:
        return jsonify({"error": "Please provide a 'word' query parameter"}), 400

    meaning = word_dict.get(word_to_search)
    if meaning:
        return jsonify({word_to_search: meaning})
    else:
        return jsonify({"message": "The given word is not in your dictionary. Go ahead and create it!"}), 404


# 📚 Get all words
@app.route('/get_all', methods=['GET'])
def get_all():
    word_dict = load_words()
    return jsonify(word_dict)

 # Update a word
@app.route('/update', methods=['PUT'])
def update_word():
    word_dict = load_words()
    data = request.get_json()
    word = data.get('word')
    meaning = data.get('meaning')

    if word not in word_dict:
        return jsonify({"error": "Word not found"}), 404

    word_dict[word] = meaning
    save_words(word_dict)
    return jsonify({"message": f"'{word}' updated successfully!"})


# ❌ Delete a word
@app.route('/delete', methods=['DELETE'])
def delete_word():
    word_dict = load_words()
    data = request.get_json()
    word = data.get('word')

    if word not in word_dict:
        return jsonify({"error": "Word not found"}), 404

    del word_dict[word]
    save_words(word_dict)
    return jsonify({"message": f"'{word}' deleted successfully!"})


# 🏠 Optional home route
@app.route('/')
def home():
    return jsonify({"message": "Adap backend is running!"})


if __name__ == '__main__':
    app.run(debug=True)

