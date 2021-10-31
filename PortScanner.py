#!/bin/python3

# Import Modules
import socket, sys, platform, argparse
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

# create parser
parser = argparse.ArgumentParser(description=colors.HEADER + "#" * 50 + '''
 ____   __  ____  ____    ____   ___   __   __ _ 
(  _ \ /  \(  _ \(_  _)  / ___) / __) / _\ (  ( \\
 ) __/(  O ))   /  )(    \___ \( (__ /    \/    /
(__)   \__/(__\_) (__)   (____/ \___)\_/\_/\_)__)
  
''' + "#" * 50 + colors.ENDC +''' 
Port Scan is a simple Python3 port scanner.
Port Scan syntax for a regular scan: ./portscan.py <IP Address> <Starting Port> <Ending Port>
Port Scan syntax for a verbose scan: ./portscan.py <IP Address> <Starting Port> <Ending Port> -v
NOTE: Verbose scanning is not reccomended on Windows machines as the built in colorizing doesn't work.
''', formatter_class=argparse.RawDescriptionHelpFormatter)

# add arguments to the parser
parser.add_argument('target', action='store', type=str, help='IP address of the target machine')
parser.add_argument('start_port', action='store', type=int, help='start of port range to scan')
parser.add_argument('end_port', action='store', type=int, help='end of port range to scan')
parser.add_argument('-v', action='store_true', required=False, help='show verbosity, colorized on Unix')

# parse the arguments
args = parser.parse_args()

# Define Target
target = socket.gethostbyname(args.target)
start_port = args.start_port
end_port = args.end_port + 1


print(colors.HEADER + "#" * 50)
print('''
 ____   __  ____  ____    ____   ___   __   __ _ 
(  _ \ /  \(  _ \(_  _)  / ___) / __) / _\ (  ( \\
 ) __/(  O ))   /  )(    \___ \( (__ /    \/    /
(__)   \__/(__\_) (__)   (____/ \___)\_/\_/\_)__)

''')
print(f"Scanning target {target}")
print(f"Time started: {str(datetime.now())}")
print("#" * 50 + colors.ENDC)

# Verbose Scanner
if args.v == True:
    try:
        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print(f"{colors.OKGREEN}[+] - Port {port} is open{colors.ENDC}")
            else:
                print(f"{colors.FAIL}[-] - Port {port} is closed{colors.ENDC}")
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
                print(f"[+] - Port {port} is open")
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
