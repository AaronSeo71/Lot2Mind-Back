from flask import Flask, request, jsonify
from flask_cors import CORS

import hashlib

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500","http://127.0.0.1:5000"])

@app.route("/")
def helloWorld():
   return "Hello, my backend!"

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    image_data = image.read()
    
    sha256_hash = hashlib.sha256(image_data).hexdigest()
    
    return jsonify({'hash': sha256_hash})

@app.route('/upload_text', methods=['POST'])
def upload_text():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    
    return jsonify({'hash': sha256_hash})

if __name__ == '__main__':
    app.run(debug=True)
