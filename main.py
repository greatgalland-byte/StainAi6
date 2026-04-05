import os
import httpx
import logging
from flask import Flask, request, jsonify, send_from_directory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder=STATIC_DIR)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"

SYSTEM_PROMPT = (
    "You are StainAI Agent — a smart, friendly, and capable AI assistant. "
    "Answer clearly and concisely. Be conversational but accurate. "
    "If you don't know something, say so honestly."
)


@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    if not GROQ_API_KEY:
        logger.error("GROQ_API_KEY is not set")
        return jsonify({"error": "API key not configured on server."}), 500

    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    try:
        with httpx.Client(timeout=30) as client:
            res = client.post(
                GROQ_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={"model": MODEL, "messages": full_messages}
            )
            logger.info(f"Groq status: {res.status_code}")
            res.raise_for_status()
            reply = res.json()["choices"][0]["message"]["content"].strip()
            return jsonify({"reply": reply})
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
        if e.response.status_code == 429:
            return jsonify({"error": "Rate limited. Try again in a moment."}), 429
        if e.response.status_code == 401:
            return jsonify({"error": "Invalid API key. Check your Groq key."}), 401
        return jsonify({"error": f"AI error ({e.response.status_code}). Try again."}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Something went wrong. Try again."}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
