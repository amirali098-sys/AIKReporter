# 🎯 AIKReporter

> A powerful and clean Telegram reporter tool for channels, accounts, and groups.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telethon](https://img.shields.io/badge/Telethon-1.34%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 About

**AIKReporter** is a lightweight command-line tool built with Python and Telethon
that allows you to report Telegram channels, accounts, and groups for various
violations (spam, pornography, violence, etc.).

It features a clean colored interface, live progress bar, FloodWait handling,
and automatic logging of all reports.

---

## ✨ Features

- 🎨 Clean colored terminal interface
- 📊 Live progress bar with speed and ETA
- 🛡️ FloodWait handling (automatic cooldown)
- 📝 Automatic log saving
- 💾 Config saving (no need to enter API credentials every time)
- 🔧 Support for 10 report reasons
- 🖥️ Works on Windows, Linux, macOS, and Termux

---

## 📋 Report Reasons

| #  | Reason           |
|----|------------------|
| 1  | Spam             |
| 2  | Pornography      |
| 3  | Violence         |
| 4  | Child Abuse      |
| 5  | Other            |
| 6  | Copyright        |
| 7  | Fake             |
| 8  | Geo Irrelevant   |
| 9  | Illegal Drugs    |
| 10 | Personal Details |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/amirali098-sys/AIKReporter.git
cd AIKReporter
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the tool

```bash
python main.py
```

---

## 🔑 First-Time Setup

On the first run, you'll be asked for:

1. **API ID** — Get it from [my.telegram.org](https://my.telegram.org)
2. **API Hash** — Same place
3. **Phone Number** — With country code (e.g. `+989123456789`)
4. **Verification Code** — Sent to your Telegram
5. **2FA Password** — If enabled

After the first run, credentials are saved to `config.json` so you don't have
to enter them again.

---

## 📁 Project Structure

```text
AIKReporter/
├── main.py               # Entry point
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
│
├── core/
│   ├── __init__.py
│   ├── client.py         # Telegram connection
│   ├── reporter.py       # Reporting logic
│   ├── config.py         # Config manager
│   └── utils.py          # Logging & progress bar
│
├── ui/
│   ├── __init__.py
│   ├── banner.py         # ASCII art & colors
│   └── menu.py           # Interactive menus
│
└── logs/
    └── reports.log       # Auto-generated
```

---

## ⚠️ Disclaimer

**This tool is provided for educational and research purposes only.**

* 🎓 **Educational Use Only** — AIKReporter is intended to demonstrate how Telegram's API works and how reporting mechanisms function. It is **not** designed for mass reporting, harassment, or abuse.
* ⚖️ **User Responsibility** — The developer of this tool is **not responsible** for any misuse, damage, or legal consequences caused by this software. **You are solely responsible** for how you use it.
* 🚫 **No Malicious Use** — Do not use this tool to:

  * Harass, threaten, or target individuals or communities.
  * Send false or malicious reports.
  * Violate Telegram's [Terms of Service](https://telegram.org/tos) or [Community Guidelines](https://telegram.org/faq#q-what-are-your-community-guidelines).
  * Break any local, national, or international laws.
* 📝 **Reporting Should Be Genuine** — Only report content that **genuinely violates** Telegram's rules. False reporting may result in your own account being **banned or restricted**.
* 🔒 **Your Account, Your Risk** — Using this tool may put your Telegram account at risk of being limited, flagged, or banned. Use at your own discretion.

**By using this software, you agree that you have read and understood this disclaimer.**

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Developer

**AmirAli (AIK)**

* GitHub: [@amirali098-sys](https://github.com/amirali098-sys)

---

⭐ If you like this project, give it a star!