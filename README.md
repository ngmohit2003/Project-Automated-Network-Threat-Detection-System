# 🛡️ Network Threat Detection System (NTDS)

A real-time Linux-based network threat detection system built using Python, Scapy, Flask, and iptables. This project captures live network traffic, detects suspicious activity like SYN floods, port scans, IP spoofing, and invalid TCP flags, and automatically blocks the attacker’s IP while providing logs, reports, and a web dashboard for monitoring.

---

## 📌 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Technologies Used](#️-technologies-used)
- [📸 Architecture](#-architecture)
- [📂 Project Structure](#-project-structure)
- [📥 Installation & Setup](#-installation--setup)
- [⚙️ How It Works](#️-how-it-works)
- [📊 Web Dashboard](#-web-dashboard)
- [🧠 Use Cases & Importance](#-use-cases--importance)
- [📝 License](#-license)

---

## 🚀 Features

- 📡 Real-time packet sniffing using Scapy
- 🧠 Intelligent threat detection:
  - SYN Floods
  - Port Scans
  - IP Spoofing
  - Invalid TCP Flag combinations
- 🔐 Auto-blocking IPs using `iptables`
- 🗂️ Logging all threats to `threats.log`
- 📊 Terminal-based report generator
- 🌐 Flask-based web dashboard with graphs
- 📁 Clean modular architecture

---

## 🛠️ Technologies Used

| Component         | Tech Used            |
|------------------|----------------------|
| Language         | Python 3             |
| Packet Sniffing  | Scapy                |
| Web Server       | Flask                |
| Charts           | Chart.js             |
| Firewall Control | iptables (Linux)     |
| UI Styling       | Bootstrap (CDN)      |
| OS               | Kali Linux / Linux   |

---

## 📸 Architecture

![Network Threat Detection System - Architecture](./images/ntds-architecture.png)

> Diagram showing the flow of data from packet capture → threat detection → logging/blocking → report/dashboard.

---

## 📂 Project Structure

NetworkThreatDetectorSystem(NTDS)/
├── main.py # Starts packet sniffer
├── detection_rules.py # Defines threat detection logic
├── logger.py # Handles alerts, logging, and IP blocking
├── report.py # Generates CLI summary from logs
├── threats.log # Log file for all alerts
├── blocked_ips.txt # List of blocked attacker IPs
├── dashboard/
│ ├── app.py # Flask server for web dashboard
│ ├── templates/
│ │ └── index.html # Web dashboard UI
│ └── static/ # (Optional) Chart.js/Bootstrap assets
└── images/
└── ntds-architecture.png # Diagram for README.md



NetworkThreatDetector/
├── dashboard/
│   ├── app.py                  ← Flask web app
│   ├── templates/
│   │   └── index.html          ← HTML page
│   └── static/
│       └── chart.js            ← Chart.js (loaded from CDN)
├── detection_rules.py
├── logger.py
├── main.py
├── blocked_ips.txt
├── threats.log
├── report.py





🔁 FULL WORKFLOW (Step-by-Step)
Here’s how your full system works from start to finish:

                ┌──────────────────────────────┐
                │          User                │
                └────────────┬─────────────────┘
                             │
                        Run main.py
                             │
               ┌────────────▼────────────┐
               │ Scapy captures packets  │ ← (sniff)
               └────────────┬────────────┘
                             │
               ┌────────────▼────────────┐
               │ detect_threats()        │ ← detection_rules.py
               │ (SYN flood? Port scan?) │
               └────────────┬────────────┘
                             │
     ┌──────────────────────▼───────────────────────┐
     │ If threat detected:                          │
     │   ├── Print alert to terminal                │
     │   ├── Log to threats.log                     │
     │   └── Block IP using iptables                │ ← logger.py
     └──────────────────────┬───────────────────────┘
                             │
         ┌──────────────────▼─────────────────┐
         │ View logs in CLI (report.py)       │
         └──────────────────┬─────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │ View graphs in browser (dashboard/)    │ ← Flask + Chart.js
        └────────────────────────────────────────┘



⚙️ How It Works
main.py starts sniffing live packets using Scapy.

Each packet is sent to detection_rules.py, where rules check for SYN floods, port scans, spoofing, and bad flags.

If a threat is found:

An alert is printed and logged (threats.log)

The source IP is blocked via iptables and saved to blocked_ips.txt

report.py can be used to generate a terminal-based report summary.

dashboard/app.py (Flask) serves a live dashboard to visualize all the threats.


🧠 Use Cases & Importance
Use Case	Description
🔍 Educational Project	Great for students learning cybersecurity and Linux
🧪 Lab/VM Threat Monitoring	Detects real attack patterns in virtual environments
🛡️ Personal Firewall	Blocks attackers before they do damage
📊 Visualization Demo	Turn boring logs into interactive graphs

✅ Why This Matters
Trains you to think like a blue-team defender

Gives you hands-on Linux + networking experience

Shows how real-world detection systems work (like Snort, Suricata)

You built something explainable, demonstrable, and portfolio-worthy


📚 RESOURCES USED:
Kali Linux

RockYou Wordlist

Python Docs

Flask Framework

OWASP Top 10



⚠️ DISCLAIMER:
CrackSuite is intended only for educational and ethical purposes. Do NOT use this tool on real systems, networks, or data without explicit permission. Misuse can be illegal.



🧑‍💻 AUTHOR:
Mohit Nigote
CyberSec & Linux Enthusiast
📧 - mohitnigote461001@gmail.com (use real if public)
💻 GitHub:- ngmohit2003.
x-x 
MN.
