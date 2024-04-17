from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Допустимый UID карты
ALLOWED_CARD_UID = "b36ff5a5"

@app.route('/card_read', methods=['POST'])
def card_read():
    # Получаем данные из POST запроса
    data = request.json
    card_id = data.get('cardId', None)
    
    # Проверяем, соответствует ли полученный UID допустимому
    if card_id == ALLOWED_CARD_UID:
        # Доступ разрешен
        return jsonify({"access": "granted"}), 200
    else:
        # Доступ запрещен для всех других UID
        return jsonify({"access": "denied"}), 200

# Запускаем сервер на всех доступных адресах на порту 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
