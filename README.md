# 🦎 LizardBot

A Telegram bot with event handling, admin commands, custom keyboards, and database support.  
Supports multiple languages (EN / RU) and works in both private chats and groups.

---

## 📌 Features
- 🗨️ Handles private & group events  
- 👮 Admin & member commands  
- 🎛️ Custom inline/reply keyboards  
- 🗂️ Organized text responses (EN / RU)  
- 💾 SQLite database support  
- ⚡ Easy setup & launch  

---

## 📂 Project Structure
- main.py — main bot logic  
- start.py — entry point (launch)  
- bot.py — bot initialization  
- db.py — database functions  
- keyboards.py — keyboard generation  
- group_events/ — event & command handlers for groups  
- utils/  
  - infoChatUser.py — chat/user info utilities  
  - permission.py — permission checks  
  - texts/ — multilingual text files (en/, ru/)  

---

## 🚀 Installation & Launch
1. Clone the repository:
   ```
   git clone https://github.com/TTI17/LizardBot-Update.git
   cd LizardBot-Update
   ```
Create & activate virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate   # Linux / MacOS
venv\\Scripts\\activate      # Windows
```
Install dependencies:
```
pip install -r requirements.txt
Run the bot:
python start.py
```
🛠 Requirements
```
Python 3.10+
aiogram
sqlite3 (built-in with Python)
```
📌 TODO / Plans
 - Add more commands for group management

 - Extend database features

 - Improve admin panel

 - Add more languages

📜 License
[MIT License](https://github.com/TTI17/LizardBot/blob/main/LICENSE)
