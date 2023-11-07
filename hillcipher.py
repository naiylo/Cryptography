# Hill-Cipher

# easy example for showing purpose

wordthatappears = "CLASSICAL"
example1Decoded = ""
example1Encoded = "ZTGHFNATGBUCKAHMOPZOUAFAJYFUR OQYHYHNML NDE  PQONFHSZCPDWZITEJSLOYWKGBEVZCTU  HMGDRQKTQKAQFTRTCQBDOUYM"

keyExample2 = [[11,3],[8,7]]
keyExample2inv = [[20,3],[8,16]]
example2Decoded = "ENDE UM ZWEI"
example2Encoded = "CPSZWYVIRDOH"
  
# help-functions

# to make it as easy as possible we use numpy and math to multiply the matrizes

import numpy as np
import math as math
import sympy as sp

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

# create the mod inverse for a given number "a" and a mod "m"
def modInverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# gives us the inverse matrix (modulo is set to 27 because we have the capital letters A-Z and the blank space)
def inverseMatrix(matrix, modulo = 27):
    matrix = np.array(matrix)
    m, n = matrix.shape
    det = int(round(np.linalg.det(matrix)))
    det_inv = modInverse(det,modulo)
    
    if det == 0 or det_inv is None:
        # Matrix is singular or doesn't have a modular inverse
        return None

    if m == n == 2:
        adjugate = np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])

    elif m == n == 3:
        adjugate = np.zeros_like(matrix)

        for i in range(3):
            for j in range(3):
                sub_matrix = np.delete(np.delete(matrix, i, 0), j, 1)
                cofactor = int(round(np.linalg.det(sub_matrix)))
                adjugate[i, j] = (-1) ** (i + j) * cofactor
    
    inverse_matrix = (det_inv * adjugate) % modulo
    
    return inverse_matrix

# lets try it on a example
#print(inverseMatrix(keyExample2))
#print(keyExample2inv)

# encoding function

def encodeHillCipher(string, keymatrix):
    keymatrix = np.array(keymatrix)
    shifted = []
    basis = convertToNumber(string)
    blocklength = keymatrix.shape[0]
    for i in range(0, len(basis), blocklength):
        # Reshape to make it a 2D matrix
        block = np.array(basis[i:i+blocklength]).reshape(-1, 1)
        encryptedblock = (keymatrix.dot(block)) % 27
        shifted += encryptedblock[:, 0].tolist()
    
    return shifted

# some tests

#print(convertToString(encodeHillCipher(example2Decoded, keyExample2)))
#print(example2Encoded)

# decoding function

def decodeHillCipher(string, keymatrix):
    keymatrix = np.array(keymatrix)
    shifted = []
    basis = convertToNumber(string)
    blocklength = keymatrix.shape[0]

    for i in range(0, len(basis), blocklength):
        block = np.array(basis[i:i+blocklength]).reshape(-1, 1)
        decryptedblock = (keymatrix.dot(block)) % 27
        decryptedblock = decryptedblock.astype(int)
        shifted += decryptedblock[:, 0].tolist()

    shifted = convertToString(shifted)
    return shifted

# some tests

#print(decodeHillCipher(example2Encoded, keyExample2inv))
#print(example2Decoded)

# if we have a encoded string and a word or sentence that we know is in the decoded string we can 
# use some methods to compute the key matrix for that we need some help functions

# function to determine if the found determinat of the found matrix is coprime with his inverted matrix
# modulo is again set to 27 (same explanation as beforehand)

def isCoprimeWithInverse(matrix, modulo=27):
    matrix = np.array(matrix)
    det = int(round(np.linalg.det(matrix)))
    det_inv = modInverse(det, modulo)

    if det == 0 or det_inv is None:
        # Matrix is singular or doesn't have a modular inverse
        return False

    gcd = math.gcd(det, modulo)

    return gcd == 1

# we can test this with our given example2
# print(isCoprimeWithInverse(keyExample2inv))

# function to return a list of possible key matrices with the input of a known word in the decoded string

# for this we need a function that gives us every possible substring with the length of the known word

def generateSubstrings(string, length):
    substrings = []
    n = len(string)

    if length <= 0 or length > n:
        return substrings  # Wenn k ungültig ist, leere Liste zurückgeben

    for i in range(n - length + 1):
        substring = string[i:i + length]
        substrings.append(substring)

    return substrings

# futhermore we need a function to generate the key if I have a string and I know the decoded string

def findCipherKey(string, known, blocklength):

    basisstring = convertToNumber(string)
    basisstring = np.array(basisstring)
    basisstring = basisstring.reshape(blocklength,blocklength).T

    print("basisstring:\n",basisstring)

    basisknown = convertToNumber(known)
    basisknown = np.array(basisknown)
    basisknown = basisknown.reshape(blocklength,blocklength).T

    print("basisknown:\n",basisknown)

    P = inverseMatrix(basisknown, 27)

    print("P:\n" ,P)

    keymatrix = np.dot(basisstring, P) % 27

    return inverseMatrix(keymatrix)

# we can test this with our given example2
#print(findCipherKey("ENDE", "CPSZ", 2))

# now a function that gives us all possible keys for all the combinations of substrings

def findPossibleKeyMatrices(string, known, blocklength, modulo=27):

    possibleKeyMatrices = []
    length = len(known)
    substrings = generateSubstrings(string, length)
    for i in substrings:
        print("fitting on substring: ",i)
        key = findCipherKey(i, known, blocklength)
        print("the possible key,\n", key)
        possibleKeyMatrices.append(key)
        try:
            print("decoded: ", decodeHillCipher(string, key))
        except:
            continue

    return possibleKeyMatrices

#print(findPossibleKeyMatrices(example2Encoded, "ENDE", 2))

# now we try a harder example

example3Encoded = "ZTGHFNATGBUCKAHMOPZOUAFAJYFUR OQYHYHNML NDE  PQONFHSZCPDWZITEJSLOYWKGBEVZCTU  HMGDRQKTQKAQFTRTCQBDOUYM"
keyExample3size = 3
wordthatappears = "CLASSICAL"

#findPossibleKeyMatrices(example2Encoded, "ENDE",2, modulo=27)
findPossibleKeyMatrices(example3Encoded, wordthatappears,keyExample3size, modulo=27)
