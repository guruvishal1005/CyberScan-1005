import socket
import ipaddress
import threading
from queue import Queue


queue = Queue()
open_ports=[]


def is_valid_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False

def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

def fill_queue(from_port,to_port):
    for i in range(from_port,to_port+1):
        queue.put(i)

def worker():
    while not queue.empty():
        port = queue.get()
        if (portscan(port)):
            print("Port {} is open".format(port))
            open_ports.append(port)





#main

print(r"""

   _____      _               _____                   __  ___   ___  _____ 
  / ____|    | |             / ____|                 /_ |/ _ \ / _ \| ____|
 | |    _   _| |__   ___ _ _| (___   ___ __ _ _ __    | | | | | | | | |__  
 | |   | | | | '_ \ / _ \ '__\___ \ / __/ _` | '_ \   | | | | | | | |___ \ 
 | |___| |_| | |_) |  __/ |  ____) | (_| (_| | | | |  | | |_| | |_| |___) |
  \_____\__, |_.__/ \___|_| |_____/ \___\__,_|_| |_|  |_|\___/ \___/|____/ 
         __/ |                                                             
        |___/                                                                                               
              [ CyberScan 1005 - Multithread Port Scanner ]
                     Developed by: GuruVishal1005
      
GitHub  : https://github.com/guruvishal1005
LinkedIn: https://www.linkedin.com/in/guruvishal-sr/
""")

target=input("Enter target IP: ")
while not is_valid_ip(target):
    target=input("Enter a valid target IP again: ")

port1 = int(input("Enter the starting port to scan: "))
port2 = int(input("Enter the ending port to scan: "))
while not(port1>0 and port2> 0 and port1<port2):
    print("Invalid port entries!! Retry")
    port1 = int(input("Enter the starting port to scan: "))
    port2 = int(input("Enter the ending port to scan: "))

fill_queue(port1,port2)

thread_list=[]

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open Ports are:", open_ports)

