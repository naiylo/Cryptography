# Affine-Cipher

# easy example that you could solve with Brute-Force

exampleEncoded = "BAOF OLAYANMAFAXSNEMGFKRSFVOHQMRZOEQYXAF XSBAMFNXCYFXTFBOXMMASFWEYOMELNASBFKROFCYOXNMLN"
exampleDecoded = "DER FRUEHESTE EINSATZ VON KRYPTOGRAPHIE FINDET SICH IM DRITTEN JAHRTAUSEND VOR CHRISTUS"
shift = 4
multiplier = 26

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

# returns a list of the numbers below a number k that dont share any divider besides 1
import math
def coprime(k):
    coprime = []
    for i in range(1,k):
        if math.gcd(k, i) == 1:
            coprime.append(i)
        else:
            continue
    return coprime

# crucial for affine Cipher to create the mod inverse for a given number "a" and a mod "m"
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# encoding function

# function to encode with a given shift and multiplier
def encodeAffineCipher(string, shift, multiplier):
    basis = convertToNumber(string)  
    shifted = [] 
    for f in basis:
        shifted.append((multiplier*f+shift)%27)
    return convertToString(shifted)


# decoding function

# brute-force function to test every posssible shift and multiply
def decodeAffineCipherBruteForce(string):
    basis = convertToNumber(string)  
    shifted = [] 
    multiplier = coprime(27)
    for a in range(1,27):
        for z in multiplier:
            b = mod_inverse(z,27)
            for f in basis:
                shifted.append((b*(f-a))%27)

            print("Shift " + str(a) + "   Multiplier: " + str(b) + "  Result: " + convertToString(shifted))
            shifted = []

# function to decode with a given shift and multiplier
def decodeAffineCipher(string, shift, multiplier):
    basis = convertToNumber(string)  
    shifted = [] 
    mod_inverse = mod_inverse(multiplier)
    for f in basis:
        shifted.append((mod_inverse*(f-shift))%27)
    return convertToString(shifted)

# some tests to see if everything works 
print("\nStart of tests\n")
print("Example: " + exampleEncoded + "\n")
print("Test of brute-force function:\n")
decodeAffineCipherBruteForce(exampleEncoded)
print("\nShift: 4 and multiplier: 26 is correct, so lets try to encode the example again")
print(encodeAffineCipher(exampleDecoded, shift, multiplier) + "\n")
print("Everything worked!\n")

        
        

