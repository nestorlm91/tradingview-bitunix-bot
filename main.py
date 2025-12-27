import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Salud / prueba (lo que ya te funciona)
@app.get("/")
def home():
    return jsonify(status="ok")

# Webhook de TradingView (aquí llegarán las señales)
@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    # Por ahora solo confirmamos que recibimos algo
    return jsonify(received=True, data=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
