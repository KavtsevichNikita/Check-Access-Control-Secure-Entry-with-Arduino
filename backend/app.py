from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Допустимый UID карты
ALLOWED_CARD_UID = "b36ff5a5"

@app.route('/card_read', methods=['POST'])
def card_read():
    data = request.json
    card_id = data.get('cardId', None)
    # Проверяем, соответствует ли полученный UID допустимому
    access = 'granted' if card_id == ALLOWED_CARD_UID else 'denied'
    socketio.emit('card_response', {'access': access})
    return jsonify({'access': access}), 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
