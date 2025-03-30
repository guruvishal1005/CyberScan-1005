# This is a simple multi-thread port scanner
# Checks the open ports of a given IP address in the specific port range
# Built using socket library
# For multithreading purpose we use Thread library

import socket
import ipaddress
import threading
from queue import Queue

# Using queue for increased efficiency
queue = Queue()
# Store open Ports
open_ports=[]


# check if user entered IP is valid
# We use ipaddress library 
def is_valid_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False

# This is the heart, the mind everything
# This thing scans for open port
# We'll be using socket to help us out
def portscan(port):
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

# This is used to fill the queue of ports to scan from the user inputed range
def fill_queue(from_port,to_port):
    for i in range(from_port,to_port+1):
        queue.put(i)


# This guy here will check if each port is open or not and append the answer to the final list
def worker():
    while not queue.empty():
        port = queue.get()
        if (portscan(port)):
            print("Port {} is open".format(port))
            open_ports.append(port)





#main

# Banner
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
print()
print()

# To get target IP
target=input("Enter target IP: ")
print()
while not is_valid_ip(target):
    target=input("Enter a valid target IP again: ")
    print()

# Getting 2 port range from user 
port1 = int(input("Enter the starting port to scan: "))
port2 = int(input("Enter the ending port to scan: "))
print()
while not(port1>0 and port2> 0 and port1<port2):
    # Checking if the entered port is valid and obeys the conditions
    print("Invalid port entries!! (Port must be > 0 && starting port > ending port) Retry")
    print()
    port1 = int(input("Enter the starting port to scan: "))
    port2 = int(input("Enter the ending port to scan: "))
    print()

# Feeding the queue with ports withing given range
fill_queue(port1,port2)

# This will contain the threads we create
thread_list=[]

# Change the range inside the for loop, to specify the amount of threads you want to use
# I'm using 10 threads because it felt faster
# This loop is to create the threads and feed it to thread_list 
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# Start all the threads
for thread in thread_list:
    thread.start()

# Join all the threads
for thread in thread_list:
    thread.join()

# Print the final list of all open ports for quick view
print("Open Ports are:", open_ports)

