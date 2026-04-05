import os
import httpx
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct:free"

SYSTEM_PROMPT = (
    "You are StainAI Agent — a smart, friendly, and capable AI assistant. "
    "Answer clearly and concisely. Be conversational but accurate. "
    "If you don't know something, say so honestly."
)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    try:
        with httpx.Client(timeout=30) as client:
            res = client.post(
                OPENROUTER_URL,
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://stainai.up.railway.app",
                    "X-Title": "StainAI Agent"
                },
                json={"model": MODEL, "messages": full_messages}
            )
            res.raise_for_status()
            reply = res.json()["choices"][0]["message"]["content"].strip()
            return jsonify({"reply": reply})
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 429:
            return jsonify({"error": "Rate limited. Try again in a moment."}), 429
        return jsonify({"error": "AI service error. Try again."}), 500
    except Exception:
        return jsonify({"error": "Something went wrong. Try again."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
