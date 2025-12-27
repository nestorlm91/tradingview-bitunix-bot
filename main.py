import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(status="ok", service="tradingview-bitunix-bot")

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True)

    # Si no llegó como JSON, intenta leer como texto y convertirlo
    if data is None:
        raw = request.get_data(as_text=True)
        try:
            data = json.loads(raw) if raw else {"raw": ""}
        except Exception:
            data = {"raw": raw}

    print("✅ WEBHOOK DATA:", data)
    return jsonify(received=True), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
