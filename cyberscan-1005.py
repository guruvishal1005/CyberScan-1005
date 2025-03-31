import socket
import ipaddress
import threading
import argparse
from queue import Queue
from termcolor import colored

queue = Queue()
open_ports = []


def is_valid_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


# ScanThread class for handling scanning and banner grabbing
class ScanThread(threading.Thread):
    def __init__(self, target, port, timeout, verbose):
        super().__init__()
        self.target = target
        self.port = port
        self.timeout = timeout
        self.verbose = verbose
        self.result = None

    def run(self):
        try:
            # Create a socket and connect to the target host and port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.target, self.port))

            # Print only if verbose is enabled
            if self.verbose:
                print(colored(f"[+] Port {self.port} is open.", "green"))

            try:
                # Banner grabbing
                sock.send(b"GET / HTTP/1.1\r\n\r\n")
                response = sock.recv(1024).decode("utf-8")

                if self.verbose:
                    print(f"Banner for port {self.port}: {response.strip()}")

                # Simple vulnerability detection (example)
                if "FTP" in response and "2.2" in response:
                    print(colored(f"[!] Vulnerability detected: FTP service version {response.strip()} is vulnerable.", "yellow"))

            except:
                if self.verbose:
                    print(f"[-] Unable to get banner for port {self.port}")

            self.result = self.port
        except:
            pass
        finally:
            sock.close()


def fill_queue(start_port, end_port):
    for port in range(start_port, end_port + 1):
        queue.put(port)


# Worker function to process the queue
def worker(target, timeout, verbose):
    while not queue.empty():
        port = queue.get()
        scanner = ScanThread(target, port, timeout, verbose)
        scanner.start()
        scanner.join()
        if scanner.result is not None:
            open_ports.append(scanner.result)


def parse_port_range(port_range):
    if port_range.lower() == 'all':
        return 1, 65535
    else:
        start_port, end_port = map(int, port_range.split('-'))
        return start_port, end_port



def main():
    print(r"""
       _____      _               _____                   __  ___   ___  _____ 
      / ____|    | |             / ____|                 /_ |/ _ \ / _ \| ____|
     | |    _   _| |__   ___ _ _| (___   ___ __ _ _ __    | | | | | | | | |__  
     | |   | | | | '_ \ / _ \ '__\___ \ / __/ _` | '_ \   | | | | | | | |___ \ 
     | |___| |_| | |_) |  __/ |  ____) | (_| (_| | | | |  | | |_| | |_| |___) |
      \_____\__, |_.__/ \___|_| |_____/ \___\__,_|_| |_|  |_|\___/ \___/|____/ 
             __/ |                                                             
            |___/                                                                                               
                          [ Multithread Port Scanner ]

    """)
    print()

    # Argument parser setup
    parser = argparse.ArgumentParser(description="CyberScan 1005 - Fast Multi-threaded Port Scanner")
    parser.add_argument('-t', '--target', required=True, help='Target IP address')
    parser.add_argument('-p', '--port-range', default='1-100', help='Port range to scan (e.g., 1-100 or all)')
    parser.add_argument('-T', '--timeout', default=1.0, type=float, help='Timeout in seconds (default: 1.0)')
    parser.add_argument('-n', '--num-threads', default=10, type=int, help='Number of threads to use (default: 10)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')  # ✅ Added verbose mode
    args = parser.parse_args()

    target = args.target
    if not is_valid_ip(target):
        print(colored("Invalid IP address. Please enter a valid IP!", "red"))
        return

    # Parse port range
    start_port, end_port = parse_port_range(args.port_range)

    # Fill queue with ports
    fill_queue(start_port, end_port)

    # Create threads
    thread_list = []
    for _ in range(args.num_threads):
        thread = threading.Thread(target=worker, args=(target, args.timeout, args.verbose))
        thread_list.append(thread)

    # Start all threads
    for thread in thread_list:
        thread.start()

    # Join all threads
    for thread in thread_list:
        thread.join()

    # Display results
    if open_ports:
        print(colored(f"\n[+] Open Ports: {open_ports}", "green"))
    else:
        print(colored("\n[-] No open ports found.", "red"))


# Run the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
    except Exception as e:
        print(f"[!] Error: {e}")
