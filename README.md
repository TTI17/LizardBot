# 🦎 LizardBot

![LizardBot](https://github.com/TTI17/LizardBot/blob/main/src/banner.jpg)

[![License](https://img.shields.io/github/license/TTI17/LizardBot)](https://github.com/TTI17/LizardBot/blob/main/LICENSE)

-----

A powerful Telegram bot with comprehensive group management features, event handling, admin commands, custom keyboards, and database support.  
Supports multiple languages (EN / RU) and works in both private chats and groups
---

## 📌 Features

- 🗨️ Advanced group event handling (member joins, leaves, restrictions)
- 👮 Comprehensive admin commands (ban, unban, mute)
- 👥 Member commands (rules, help, report)
- 🎛️ Custom inline/reply keyboards with intuitive UI
- 🌍 Multilingual support (English/Russian)
- 💾 SQLite database integration for data persistence
- ⚡ Easy setup & launch with virtual environment support

---

## 🚀 Installation & Launch

### 1. Clone the repository

```bash
git clone https://github.com/TTI17/LizardBot.git
cd LizardBot
```

### 2. Create and activate virtual environment (recommended)

```bash
python -m venv venv

# On Linux/MacOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with your Telegram bot token:

```
TOKEN=your_telegram_bot_token_here
```

### 5. Run the bot

```bash
python main.py
```

---

## 🤖 Bot Commands

### Admin Commands (in groups)

- `/ban` - Ban a user (reply to their message)
- `/unban` - Unban a user (reply to their message)
- `/mute` - Mute a user for 10 minutes (reply to their message)

### Member Commands

- `/start` - Start the bot (private chat only)
- `/help` - Show help information
- `/rules` - Display group rules
- `/report` - Report a message to admins (reply to the message)
- `/get_help` - Get help information

---

## 🧠 Key Features

### Event Handling

- Automatic welcome messages for new members
- Admin notifications when users join or leave
- Member status change tracking (join, leave, restriction)

### Database Integration

- Chat information storage
- User information tracking
- Message logging capabilities

### Multilingual Support

- Full support for English and Russian languages
- Easy extensibility for additional languages

### Permission System

- Robust admin permission checking
- Member status verification
- Secure command access control

---

## 📌 TODO / Plans

- [ ] Add more commands for group management
- [ ] Extend database features with analytics
- [ ] Add media content filtering capabilities
- [ ] Create web-based dashboard for bot management

---

## 📜 License

[MIT License](https://github.com/TTI17/LizardBot/blob/main/LICENSE)
