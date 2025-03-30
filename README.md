# CyberScan 1005 - Multithread Port Scanner 🔍

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/guruvishal1005/CyberScan-1005.svg)](https://github.com/guruvishal1005/CyberScan-1005/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/guruvishal1005/CyberScan-1005.svg)](https://github.com/guruvishal1005/CyberScan-1005/issues)

A **fast**, **multi-threaded** port scanner built in Python to check open ports on a target IP address within a specified range. 

```python
   _____      _               _____                   __  ___   ___  _____ 
  / ____|    | |             / ____|                 /_ |/ _ \ / _ \| ____|
 | |    _   _| |__   ___ _ _| (___   ___ __ _ _ __    | | | | | | | | |__  
 | |   | | | | '_ \ / _ \ '__\___ \ / __/ _` | '_ \   | | | | | | | |___ \ 
 | |___| |_| | |_) |  __/ |  ____) | (_| (_| | | | |  | | |_| | |_| |___) |
  \_____\__, |_.__/ \___|_| |_____/ \___\__,_|_| |_|  |_|\___/ \___/|____/ 
         __/ |                                                             
        |___/                                                                                               
              [ CyberScan 1005 - Multithread Port Scanner ]
```

---

## 📌 Features
- **Multi-threaded scanning** (10 threads by default for faster results)
- **IP validation** to ensure correct target input
- **Custom port range** scanning (supports any valid range)
- **Real-time open port detection** with clear output
- **Lightweight & easy to use** (no external dependencies)

---

## 🤷‍♂️ Why I Built This (A Teenager's Honest Confession)

Look, I'm just a college cybersecurity noob who:

1. **Needed street cred** - Wanted to impress my Discord hacking group (they weren't impressed)  
2. **Got tired of NMAP** - "But can you make your own scanner?" Challenge accepted!  
3. **Misunderstood 'network penetration testing'** - Turns out my router doesn't count as "enterprise infrastructure"  
4. **Wanted to feel cool** - Black terminal > GUI any day (until you get 100 connection timeouts)  

*"My professor said 'think outside the box'... so I built a box scanner instead."*  

⚠️ **Disclaimer**:  
This tool may:  
- Make you look 1337 in front of non-tech friends  
- Annoy your home router  
- Not actually help with your networking homework (but try telling that to my GitHub commits)  

Built with ❤️, caffeine, and questionable life choices.


## ⚙️ Installation
```bash
git clone https://github.com/guruvishal1005/CyberScan-1005.git
cd CyberScan-1005
python CyberScan_1005.py
```

---

## 🚀 Usage
1. Enter the target IP (e.g., `192.168.1.1`)
2. Specify the port range (e.g., start: `1`, end: `1000`)
3. Wait for the scan to complete
4. View open ports in real-time and final results

**Example Output**:
```
Port 22 is open
Port 80 is open
Open Ports are: [22, 80]
```

---

## ⚡️ Performance Tips
- To **increase speed**, raise the thread count (modify `range(10)` in the code)
- To **scan fewer ports**, narrow the port range (e.g., `1-1024` for common ports)

---

## 🤝 Contributing
1. Fork the project
2. Create a branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.

---

## 👨‍💻 Developer
**GuruVishal SR**  
[![GitHub](https://img.shields.io/badge/GitHub-guruvishal1005-blue)](https://github.com/guruvishal1005)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-guruvishal--sr-blue)](https://linkedin.com/in/guruvishal-sr)

---

> **Note**: Use responsibly! Only scan networks you own or have permission to test.
