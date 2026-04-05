# StainAI Agent 🤖

A sleek web-based AI chat powered by Groq (Llama 3.1). iOS-style chat bubbles, conversation memory, dark UI with red branding, and smart rate limit handling.

## Features
- 💬 iOS-style chat bubbles
- 🧠 Conversation memory per session
- ⚡ Typing indicator
- 💡 Suggestion prompts on welcome screen
- ☰ Hamburger menu with Clear Chat + Contact
- ⏳ Rate limit countdown with auto-retry
- 🆓 100% free — Flask + Groq free tier

## Setup

### 1. Get Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up → **API Keys** → **Create API Key**
- Free, no payment or card needed

---

## Deployment

### 🚂 Railway (Recommended)
1. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**
2. Connect this repo
3. Go to **Variables** tab and add:
```
GROQ_API_KEY=your_key_here
```
4. Railway auto-detects the start command via `Procfile`
5. Go to **Settings** → **Networking** → **Generate Domain**
6. Your app is live at `https://your-app.up.railway.app` 🚀

---

### 🎨 Vercel
1. Go to [vercel.com](https://vercel.com) → **Add New Project** → Import your GitHub repo
2. Add environment variable:
```
GROQ_API_KEY=your_key_here
```
3. Add a `vercel.json` file to your repo:
```json
{
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```
4. Click **Deploy**
5. Vercel gives you a free URL at `https://your-app.vercel.app` 🚀

> ⚠️ Note: Vercel runs Flask as serverless functions. The app works but cold starts may cause a slight delay on first load.

---

### 🟣 Render
1. Go to [render.com](https://render.com) → **New** → **Web Service**
2. Connect your GitHub repo
3. Fill in settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
4. Add environment variable:
```
GROQ_API_KEY=your_key_here
```
5. Click **Create Web Service**
6. Render gives you a URL at `https://your-app.onrender.com` 🚀

> ⚠️ Note: Render free tier spins down after 15 minutes of inactivity. First request after sleep takes ~30 seconds to wake up. Use UptimeRobot to ping `/` every 5 minutes to keep it awake.

---

## File Structure
```
main.py              ← Flask backend (API + static file serving)
requirements.txt     ← Python dependencies
nixpacks.toml        ← Forces Python 3.11 on Railway
Procfile             ← Start command for Railway/Render
README.md            ← This file
static/
  index.html         ← Full chat UI (frontend)
```

## Environment Variables
| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

## Stack
- Python 3.11
- Flask + httpx
- Groq API — `llama-3.1-8b-instant` (free)
- Vanilla HTML / CSS / JS frontend
- No database — sessions are in-memory

---

## Developer

**Stain**
🔗 [linktr.ee/iamevanss](https://linktr.ee/iamevanss)
