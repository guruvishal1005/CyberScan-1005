# CyberScan 1005 - Multithread Port Scanner

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![GitHub stars](https://img.shields.io/github/stars/guruvishal1005/CyberScan-1005.svg)](https://github.com/guruvishal1005/CyberScan-1005/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/guruvishal1005/CyberScan-1005.svg)](https://github.com/guruvishal1005/CyberScan-1005/issues)

```python
   _____      _               _____                   __  ___   ___  _____ 
  / ____|    | |             / ____|                 /_ |/ _ \ / _ \| ____|
 | |    _   _| |__   ___ _ _| (___   ___ __ _ _ __    | | | | | | | | |__  
 | |   | | | | '_ \ / _ \ '__\___ \ / __/ _` | '_ \   | | | | | | | |___ \ 
 | |___| |_| | |_) |  __/ |  ____) | (_| (_| | | | |  | | |_| | |_| |___) |
  \_____\__, |_.__/ \___|_| |_____/ \___\__,_|_| |_|  |_|\___/ \___/|____/ 
         __/ |                                                             
        |___/                                                                                               
                     [ Multithread Port Scanner ]
```

---

##  Features

-  Multithreaded scanning for fast results
-  Banner grabbing for service detection
-  Simple vulnerability detection
-  Customizable timeout and thread count
-  Verbose mode for detailed output

##  Installation

### Prerequisites

Ensure you have Python installed (Python 3.x recommended). You can check your Python version with:

```sh
python --version
```

### Clone the Repository

```sh
git clone https://github.com/guruvishal1005/cyberscan1005.git
cd cyberscan1005
```

### Install Dependencies

Use the following command to install the required dependencies:

```sh
pip install -r requirements.txt
```

##  Usage

Run the script with the following command:

```sh
python3 cyberscan-1005.py -t <TARGET_IP> -p <PORT_RANGE> -T <TIMEOUT> -n <NUM_THREADS> -v
```

### 🔹 Example Commands

#### Scan a specific range of ports (1-100) on a target IP
```sh
python3 cyberscan-1005.py -t 192.168.1.1 -p 1-100
```

#### Scan all ports on a target IP with a timeout of 2 seconds
```sh
python3 cyberscan-1005.py -t 192.168.1.1 -p all -T 2
```

#### Scan with 20 threads for faster results
```sh
python3 cyberscan-1005.py -t 192.168.1.1 -p 1-500 -n 20
```

#### Enable verbose mode for detailed output
```sh
python3 cyberscan-1005.py -t 192.168.1.1 -p 1-100 -v
```

###  Command-Line Options

|  Option |  Description |
|--------|-------------|
| `-t, --target` |  Target IP address |
| `-p, --port-range` |  Port range to scan (e.g., 1-100 or 'all') |
| `-T, --timeout` |  Timeout in seconds (default: 1.0) |
| `-n, --num-threads` |  Number of threads to use (default: 10) |
| `-v, --verbose` |  Enable verbose output |

##  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

##  Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

Built with ❤️, caffeine, and questionable life choices.


> **Note**: This tool is intended for educational and security research purposes only. Unauthorized use against systems without permission is illegal and strictly prohibited.

