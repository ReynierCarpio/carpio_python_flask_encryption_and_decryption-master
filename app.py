from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)


key = Fernet.generate_key()  
cipher_suite = Fernet(key)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        # Get the data to encrypt from the POST request
        data = request.json
        text = data['text']
        
        # Encrypt the text
        encrypted_text = cipher_suite.encrypt(text.encode())
        
        return jsonify({"encrypted_text": encrypted_text.decode()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        # Get the encrypted text from the POST request
        data = request.json
        encrypted_text = data['encrypted_text']
        
        # Decrypt the text
        decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
        
        return jsonify({"decrypted_text": decrypted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

