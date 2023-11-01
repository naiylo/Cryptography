# Shift-Cipher

# easy example that you could solve with Brute-Force

exampleEncoded = "VBI DZRBL STPKTCDKOTPKGTCCPYCNSLQDKOPBKFPBCNSWEPCCPWEYRKFZYKTYQZBXLDTZY"
exampleDecoded = "KRYPTOGRAPHIE IST DIE WISSENSCHAFT DER VERSCHLUESSELUNG VON INFORMATION"
shiftCipher = 16

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

def encodeShiftCipher(c, i):
    # convert input string to ASCII numbers
    basis = convertToNumber(c)  
    shifted = [] 
    for j in basis:
      shifted.append((j-i)%27)
    return convertToString(shifted)

# decoding function

# brute-force function to test every possible shift
def decodeShiftCipherBruteForce(c):
    # convert input string to ASCII numbers
    basis = convertToNumber(c)  
    shifted = []
    # try every possible shift-number i 
    for i in range(1,26):
        for j in basis:
            shifted.append((j+i)%27)

        print(str(i) + ": " + convertToString(shifted))
        shifted = []

# function to shift the string with a given shift length
def decodeShiftCipher(c, i):
    # convert input string to ASCII numbers
    basis = convertToNumber(c)  
    shifted = [] 
    for j in basis:
      shifted.append((j+i)%27)
    return convertToString(shifted)

# some tests to see if everything works 
print("\nStart of tests\n")
print("Example: " + exampleEncoded + "\n")
print("Test of brute-force function:\n")
decodeShiftCipherBruteForce(exampleEncoded)
print("\nNumber: 16  is correct, so lets try to encode the example again")
print(encodeShiftCipher(exampleDecoded, shiftCipher) + "\n")
print("Everything worked!\n")
      

