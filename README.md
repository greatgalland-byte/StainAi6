# StainAI Agent 🤖

A sleek web-based AI chat interface powered by OpenRouter (Mistral 7B). WhatsApp/Telegram style bubbles, conversation memory, and a clean dark UI.

## Features
- 💬 Chat bubble UI (WhatsApp/Telegram style)
- 🧠 Conversation memory per session
- ⚡ Typing indicator
- 💡 Suggestion prompts on welcome screen
- 🎨 StainAI branding with generated logo
- 🆓 100% free — Flask + OpenRouter free tier

## Setup

### 1. Get OpenRouter API key
- Go to [openrouter.ai](https://openrouter.ai)
- Sign up → **Keys** → **Create Key**
- Free tier, no payment needed

### 2. Deploy on Railway
- Create a new project → **Deploy from GitHub repo**
- Connect this repo
- Add environment variable:
```
OPENROUTER_API_KEY=your_key_here
```
- Set start command: `python main.py`
- Deploy!

### 3. Access
Railway gives you a public URL like:
```
https://stainai-agent.up.railway.app
```
Share it with anyone — no install needed.

## File Structure
```
main.py          ← Flask backend (API + serves frontend)
requirements.txt ← Dependencies
nixpacks.toml    ← Forces Python 3.11 on Railway
static/
  index.html     ← Full chat UI
```

## Stack
- Python 3.11
- Flask (backend + static file serving)
- httpx (API calls)
- OpenRouter — mistralai/mistral-7b-instruct:free
- Vanilla HTML/CSS/JS frontend
- Deployed on Railway
