#!/bin/python3

# Import Modules
import socket
import sys
from datetime import datetime

# Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguments.")
    print("Syntax: PortScanner.py <IP>")

# Banner
print("#" * 50)
print("Scanning target {}".format(target))
print("Time started: {}".format(str(datetime.now())))
print("#" * 50)

# Scanner
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open.".format(port))
        s.close()

# Errors
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
