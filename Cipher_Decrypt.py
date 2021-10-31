#!/bin/python3

# Import Modules
import platform, argparse

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

header = print(colors.HEADER + "#" * 42 +
"""
 ____  ____   ___  ____  _  _  ____  ____ 
(    \(  __) / __)(  _ \( \/ )(  _ \(_  _)
 ) D ( ) _) ( (__  )   / )  /  ) __/  )(  
(____/(____) \___)(__\_)(__/  (__)   (__) 

""" + "#" * 42 + colors.ENDC)

# create parser
parser = argparse.ArgumentParser(description=header, formatter_class=argparse.RawDescriptionHelpFormatter)

# add arguments to the parser
parser.add_argument('-t', type=str, required=False)

# parse the arguments
args = parser.parse_args()

# Set lists for decrytpion and encryption
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rot13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
caesar = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C']
decrypt = []

# Banner
header

# Take text input
if args.t == None:
    text = input ("Enter text string: ")
else:
    text = open(args.t).read()

# Options
encrypt_type = input ("\n1. ROT13\n2. Caesar (ROT3) Cipher\nEnter a number: ")
if encrypt_type == "1":
    encrypt_dir = input ("\n1. Cleartext to ROT13\n2. ROT13 to Cleartext\nEnter a number: ")
    if encrypt_dir == "1":
        for letter in text:
            if letter == " ":
                decrypt += " "
            elif letter == "!" or letter == "@" or letter == "#" or letter == "$" or letter == "%" or letter == "^" or letter == "&" or letter == "*" or letter == "(" or letter == ")" or letter == "~" or letter == "`" or letter == "-" or letter == "_" or letter == "+" or letter == "=" or letter == "[" or letter == "]" or letter == "{" or letter == "}" or letter == "|" or letter == "\\" or letter == ":" or letter == ";" or letter == "'" or letter == "\"" or letter == "," or letter == "." or letter == "<" or letter == ">" or letter == "?" or letter == "/":
                decrypt += letter
            elif letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "0":
                decrypt += letter
            else:
                index = alpha.index(letter)
                decrypt += rot13[index]
    elif encrypt_dir == "2":
        for letter in text:
            if letter == " ":
                decrypt += " "
            elif letter == "!" or letter == "@" or letter == "#" or letter == "$" or letter == "%" or letter == "^" or letter == "&" or letter == "*" or letter == "(" or letter == ")" or letter == "~" or letter == "`" or letter == "-" or letter == "_" or letter == "+" or letter == "=" or letter == "[" or letter == "]" or letter == "{" or letter == "}" or letter == "|" or letter == "\\" or letter == ":" or letter == ";" or letter == "'" or letter == "\"" or letter == "," or letter == "." or letter == "<" or letter == ">" or letter == "?" or letter == "/":
                decrypt += letter
            elif letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9" or letter == "0":
                decrypt += letter
            else:
                index = rot13.index(letter)
                decrypt += alpha[index]
    else:
        print(f"{colors.FAIL}Invalid entry.{colors.ENDC}")
elif encrypt_type == "2":
    encrypt_dir = input ("\n1. Cleartext to Caesar\n2. Caesar to Cleartext\nEnter a number: ")
    if encrypt_dir == "1":
        for letter in text:
            if letter == " ":
                decrypt += " "
            else:
                index = alpha.index(letter)
                decrypt += caesar[index]
    elif encrypt_dir == "2":
        for letter in text:
            if letter == " ":
                decrypt += " "
            else:
                index = caesar.index(letter)
                decrypt += alpha[index]
    else:
        print(f"{colors.FAIL}Invalid entry.{colors.ENDC}")
print ("\nOutput:\n" + ''.join(decrypt))
