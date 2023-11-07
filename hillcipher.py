# Hill-Cipher

# easy example that you could solve with Brute-Force

wordthatappears = "CLASSICAL"
example1Decoded = ""
example1Encoded = "ZTGHFNATGBUCKAHMOPZOUAFAJYFUR OQYHYHNML NDE PQONFHSZCPDWZITEJSLOYWKGBEVZCTU HMGDRQKTQKAQFTRTCQBDOUYM"

keyExample2 = [[11,8],[3,7]]
example2Decoded = "ENDE UM ZWEI"
example2Encoded = "CPSZWYVIRDOH"

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
    shifted = []
    keymatrixinv = np.linalg.inv(keymatrix)
    basis = convertToNumber(string)
    blocklength = keymatrix.shape[0]
    for i in range(0, len(string), blocklength):
        block = np.array(string[i:i+blocklength])
        decrypted_block = (keymatrixinv.dot(block)) % 26
        shifted += list(decrypted_block)
    
    # Konvertiere die Zahlen zurück in Buchstaben
    plaintext = ''.join([chr(int(char) + ord('A')) for char in plaintext])
    
    return plaintext


    
