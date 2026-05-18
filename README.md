# Cisco Telnet Multi-Device Automation

A lightweight, asynchronous Python script to connect to multiple Cisco devices via Telnet, login automatically, run commands (e.g., `show version`), and retrieve outputs.

---

## 📋 Overview

This project automates the process of connecting to multiple Cisco routers/switches using **Telnet** and **asyncio**. It is ideal for small-to-medium lab environments or simple network inventory/monitoring tasks where SSH is not available or enabled.

The script logs in with provided credentials, enters enable mode, executes commands, and displays the output for each device.

---

## ✨ Features

- **Asynchronous Telnet connections** using `telnetlib3`
- Support for **multiple devices** (easily scalable)
- Automatic login + enable mode
- Command execution and output capture
- Clean error handling (timeout, connection refused, etc.)
- Simple configuration via lists and constants

---

```
enable
configure terminal

enable secret cisco123

username admin password cisco123

line vty 0 4
login local
transport input telnet
exit
end

write memory
```

## 🛠️ Requirements

- Python 3.8+
- `telnetlib3` library

### Installation

```bash
pip install telnetlib3
