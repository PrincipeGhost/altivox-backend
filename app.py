from flask import Flask, request, jsonify
from flask_cors import CORS
CORS(app)
from iqoptionapi.stable_api import IQ_Option
import os

app = Flask(__name__)
# Puedes permitir todas las solicitudes de cualquier origen con CORS(app)
# O, para mayor seguridad, especificar únicamente tu dominio:
CORS(app, origins=["https://proyecto-b1bf7.web.app"])

@app.route('/')
def home():
    return jsonify({"message": "Altivox backend is running 🚀"})

@app.route('/connect', methods=['POST'])
def connect():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    try:
        I_want_money = IQ_Option(email, password)
        status, reason = I_want_money.connect()
        if status:
            return jsonify({"success": True, "message": "✅ Conexión exitosa con IQ Option"})
        else:
            return jsonify({"success": False, "message": "❌ Falló la conexión: " + str(reason)}), 401
    except Exception as e:
        return jsonify({"success": False, "message": f"❌ Error: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
