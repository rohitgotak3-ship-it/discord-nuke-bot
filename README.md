# Discord Nuke Bot 🚀

Ek powerful Discord bot jo `/nuke` command use करके सभी channels को delete कर सकता है।

## Features ✨

- `/nuke` - सभी channels को एक साथ delete करता है
- Admin-only command - सिर्फ server administrators use कर सकते हैं
- Fast deletion - सभी channels quickly delete हो जाते हैं
- Error handling - सुरक्षित और reliable

## Setup 🔧

### 1. Discord Bot बनाओ
1. [Discord Developer Portal](https://discord.com/developers/applications) पर जाओ
2. "New Application" click करो
3. Bot का नाम दो
4. "Bot" section में जाओ और "Add Bot" click करो
5. Token copy करो (SECRET रखो!)

### 2. Bot Permissions दो
1. OAuth2 → URL Generator में जाओ
2. Scopes: `bot` select करो
3. Permissions: 
   - `Administrator` ✓
4. Generated URL से अपने server में bot add करो

### 3. Local Setup करो (Testing के लिए)
```bash
# Clone repo
git clone https://github.com/rohitgotak3-ship-it/discord-nuke-bot.git
cd discord-nuke-bot

# Install dependencies
pip install -r requirements.txt

# .env file बनाओ
cp .env.example .env
# .env में अपना DISCORD_TOKEN डालो

# Bot run करो
python bot.py
```

### 4. Bot-Hosting.net पर Deploy करो
1. bot-hosting.net पर जाओ
2. GitHub repository import करो
3. Deploy करो
4. 24/7 online रहेगा!

## Usage 📝

```
/nuke
```

⚠️ **WARNING**: यह command सभी channels delete कर देगा! सावधानी से use करो!

## Permissions Required ⚙️

- Administrator
- Manage Channels
- Delete Channel

## Support 🆘

Koई issue आए तो GitHub issues पर बताओ!
