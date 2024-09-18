from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from oracle import GeminiOracle
import time

app = Flask(__name__, static_folder='static')
CORS(app)  # This allows your frontend to make requests to this server

oracle = GeminiOracle()  # Global instance

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/init', methods=['GET'])
def init():
    time.sleep(0.3) 
    return jsonify({
        'response': f"Welcome! I'm {oracle.name}. I am here to provide whatever solutions you may need. What do you desire?",
        'terminate': False
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    
    if user_message.lower() in ['quit', 'exit', 'bye']:
        oracle.clear_history()
        return jsonify({'response': f"{oracle.name}: Blessings", 'terminate': True})
    
    response = oracle.respond(user_message)
    return jsonify({'response': response, 'terminate': False})

if __name__ == '__main__':
    app.run(debug=True) 






