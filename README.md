# StainAI Agent 🤖

A sleek web-based AI chat powered by Groq (Llama 3.1). WhatsApp/Telegram style iOS bubbles, conversation memory, dark UI with red branding.

## Features
- 💬 iOS-style chat bubbles
- 🧠 Conversation memory per session
- ⚡ Typing indicator
- 💡 Suggestion prompts on welcome screen
- ☰ Hamburger menu with Clear Chat + Contact
- 🆓 100% free — Flask + Groq free tier

## Setup

### 1. Get Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up → **API Keys** → **Create API Key**
- Free, no payment needed

### 2. Deploy on Railway
- New project → Deploy from GitHub repo
- Connect this repo
- Add environment variable:
```
GROQ_API_KEY=your_key_here
```
- Railway auto-detects start command via Procfile
- Deploy!

## File Structure
```
main.py
requirements.txt
nixpacks.toml
Procfile
README.md
static/
  index.html
```

## Stack
- Python 3.11
- Flask + httpx
- Groq API — llama-3.1-8b-instant (free)
- Vanilla HTML/CSS/JS
- Deployed on Railway
