# Hill-Cipher

# easy example that you could solve with Brute-Force

wordthatappears = "CLASSICAL"
example1Decoded = ""
example1Encoded = "ZTGHFNATGBUCKAHMOPZOUAFAJYFUR OQYHYHNML NDE PQONFHSZCPDWZITEJSLOYWKGBEVZCTU HMGDRQKTQKAQFTRTCQBDOUYM"

keyExample2 = [[11,3],[8,7]]
keyExample2inv = [[20,13],[8,27]]
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
    for i in range(0, len(basis), blocklength):
        # Reshape to make it a 2D matrix
        block = np.array(basis[i:i+blocklength]).reshape(-1, 1)
        encryptedblock = (keymatrix.dot(block)) % 27
        shifted += encryptedblock[:, 0].tolist()
    
    return shifted

# decoding function

def decodeHillCipher(string, keymatrix):
    shifted = []
    keymatrixinv = np.linalg.inv(keymatrix)
    basis = convertToNumber(string)
    blocklength = keymatrix.shape[0]

    for i in range(0, len(basis), blocklength):
        block = np.array(basis[i:i+blocklength]).reshape(-1, 1)
        print("block: ", block)
        decryptedblock = (keymatrixinv.dot(block)) % 27
        decryptedblock = decryptedblock.astype(int)
        print("decryptedblock: ",decryptedblock)
        shifted += decryptedblock[:, 0].tolist()

    shifted = convertToString(shifted)
    return shifted

print(example2Decoded)
decodeHillCipher(example2Encoded, np.linalg.inv(np.array([20,13],[8,27])))



    
