# Maltego for Termux

A lightweight, open-source intelligence (OSINT) tool inspired by Maltego, designed to run in Termux on Android.

---

## 🛠️ Features
- Entity-based data collection (Person, Domain, IP, Email, etc.)
- Built-in transforms (WHOIS, DNS, Google search)
- Graph visualization of relationships
- Modular design for custom transforms

---

## 📥 Installation

### 1. Install Termux
Download [Termux](https://termux.com/) from F-Droid (recommended) or the Play Store.

### 2. Update & Install Dependencies
```bash
pkg update && pkg upgrade
pkg install python git
pip install networkx matplotlib requests beautifulsoup4 dnspython python-whois
