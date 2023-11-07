# Hill-Cipher

# easy example that you could solve with Brute-Force

wordthatappears = "CLASSICAL"
example1Decoded = ""
example1Encoded = "ZTGHFNATGBUCKAHMOPZOUAFAJYFUR OQYHYHNML NDE PQONFHSZCPDWZITEJSLOYWKGBEVZCTU HMGDRQKTQKAQFTRTCQBDOUYM"

# help-functions

# converts a string of capital letters to their fitting ASCII number
def convertToNumber(string):
    result = []
    for c in string:
        if c == " ":
            result.append(26)
        else:
            result.append(ord(c)-65)
    return result

# converts a list of ASCII numbers to their fitting capital letters
def convertToString(list):
    result = ""
    for c in list:
        if c == 26:
            result = result + ' '
        else:
            result = result + chr(c+65)
    return result

# encoding function

import numpy as np

def encodeHillCipher(string, keymatrix):
    result = []
    keymatrixinv = np.linalg.inv(keymatrix)
    return result