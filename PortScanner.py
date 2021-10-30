#!/bin/python3

# Import Modules
import socket
import sys
import platform
from datetime import datetime

# Set Variables
verbose = False
if platform.system() == "Windows":
    class colors:
        HEADER = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
else:
    class colors:
        HEADER = '\033[95m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'


# Define Target
if len(sys.argv) == 5:
    if sys.argv[4] == "-v":
        verbose = True
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3]) + 1
    else: 
        print("Invaild argument. Use -v for verbose")
elif len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3]) + 1
elif len(sys.argv) == 3:
    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    print("Detected target of {} and starting at port {}".format(target, start_port))
    end_port = int(input("Stop at what port number?: ")) + 1
elif len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    print("Detected target of {}".format(target))
    start_port = int(input("Start at what port number?: "))
    end_port = int(input("Stop at what port number?: ")) + 1

else:
    print("Invalid number of arguments.")
    print("Syntax: PortScanner.py <IP> <Start Port> <End Port>")

# Banner
print(colors.HEADER + "#" * 50)
print('''
 ____   __  ____  ____    ____   ___   __   __ _ 
(  _ \ /  \(  _ \(_  _)  / ___) / __) / _\ (  ( \\
 ) __/(  O ))   /  )(    \___ \( (__ /    \/    /
(__)   \__/(__\_) (__)   (____/ \___)\_/\_/\_)__)

''')
print("Scanning target {}".format(target))
print("Time started: {}".format(str(datetime.now())))
print("#" * 50 + colors.ENDC)

# Verbose Scanner
if verbose == True:
    try:
        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"{colors.OKGREEN}Port {port} is open.{colors.ENDC}")
            else:
                print("Port {} is closed".format(port))
            s.close()

    # Errors
    except KeyboardInterrupt:
        print(f"{colors.WARNING}Exiting...{colors.ENDC}")
        sys.exit()

    except socket.gaierror:
        print(f"{colors.WARNING}Hostname could not be resolved. Exiting...{colors.ENDC}")
        sys.exit()

    except socket.error:
        print(f"{colors.WARNING}Couldn't connect to server. Exiting...{colors.ENDC}")
        sys.exit()    


# Regular Scanner
else:
    try:
        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port {} is open.".format(port))
            s.close()

    # Errors
    except KeyboardInterrupt:
        print(f"{colors.WARNING}Exiting...{colors.ENDC}")
        sys.exit()

    except socket.gaierror:
        print(f"{colors.WARNING}Hostname could not be resolved. Exiting...{colors.ENDC}")
        sys.exit()

    except socket.error:
        print(f"{colors.WARNING}Couldn't connect to server. Exiting...{colors.ENDC}")
        sys.exit()  

    print("Scan complete. If no ports listed above nothing in range was open. Exiting...")
