# Viginer-Cipher

# easy example that you could solve with Brute-Force

key1 = "A KEY"
example1Decoded = "INFORMATIK BRAUCHT MATHEMATIK"
example1Encoded = "IMPSOM CMH AAERCGCDJASRIJASSO"

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

# converts key to numbers

def keytocode(k):
    keys = []
    for i in k:
        keys.append(convertToNumber(i))
    return keys

# encoding function

def encodeVigenereCipher(c,k):
    keys = keytocode(k)
    counter = 0
    modulo = len(keys)
    basis = convertToNumber(c)
    shifted = []
    for i in basis:
        index = counter % modulo
        shifter = keys[index][0]
        shifted.append((i + shifter) % 27)
        counter += 1
    return convertToString(shifted)

# decoding function

def decodeVigenereCipher(c,k):
    keys = keytocode(k)
    counter = 0
    modulo = len(keys)
    basis = convertToNumber(c)
    shifted = []
    for i in basis:
        index = counter % modulo
        shifter = keys[index][0]
        shifted.append((i - shifter) % 27)
        counter += 1
    return convertToString(shifted)

# print(encodeVigenereCipher(example1Decoded, key1))
# print(decodeVigenereCipher(example1Encoded, key1))

# longer example

example2Encoded = "NRPOYBVXBBWSJZPHSSSDXHXKCQWIJNUHVDLBQHYD WOQFASMFVFHXAJMB LYAZBVSODIXKAYSFBSAOJZJORJOZQTFNFVIHCESVDOOHAUBBS OTEPFWBTETSHXUXTDSUJOCESMYYBAFMYBOCEHFQCZEKFEXXFHIQTESJPYWDEOZ WSSSDDTKSCPQOTHMYXKXAXQFBSPOHBXVVODXKGNNZBGSASTEHS YVD AQRQTPJNFVFHXERZKOEOXKB DSJIVGLSWVXJXEFVKSXGJMRFWSXQFBSRSVPTJNIVFHSJDHATFNQHLGKSJWLFLFMYOXLGOQFBSROHXATGRVJPLWBTETFNUHVDLBQHYD WOQDTEOMYQOFBCMBBWWQVOKXWBVXVXFMYYWSRSVPOBSNE WSADHXXENQVETA ODXSASJUBILFMYBBS KTEHXAJHBVXAJXBQJODTEONBXQBXFSWQY KNODFVEOJSBZTAXJBBSFHIQTENFVIR SBQAIJQRQAPKNDBQFTNBOPHX JXBZFOMAQOOHAUBOSN"

# to analyse such a long example we need some tools to get some hints about the blocklenght and indizes
# given is the most commen triple that we can use to analyze the block lenght "FBS" "FMY"


# help function to analyze the positions of the most accuring triple and calculate the space between them

def analyzeCipher(string, keyword):
    positions = []
    distances = []

    index = -1
    while True:
        index = string.find(keyword, index + 1)
        if index == -1:
            break
        else:
            positions.append(index)
    
    for i in range(len(positions)-1):
        for j in range(i+1, len(positions)):
            distances.append(positions[j] - positions[i])
    
    return positions, distances

# print the given positions and distances to analyze the block lenght

FBS_positions, FBS_distances = analyzeCipher(example2Encoded, "FBS")
FMY_positions, FMY_distances = analyzeCipher(example2Encoded, "FMY")

print("FBS in position:", FBS_positions)
print("Distances between FBS:", FBS_distances)
print("FMY in position:", FMY_positions)
print("Distances between FMY:", FMY_distances)

# for that we create a help function that computes the number of most common divider

import math

def mostCommonDivider(list):
    biggest = math.sqrt(max(list))
    divider = []
    for i in range(2,int(biggest)):
        count = 0
        for j in list:
            if j % i == 0:
                count += 1
        if count > 0:
            divider.append((i,count))   
    return sorted(divider, key=lambda x: x[1], reverse=True) 

# print the list of dividers

FBS_mostCommonDivider = mostCommonDivider(FBS_distances)
FMY_mostCommonDivider = mostCommonDivider(FMY_distances)

print("Most common divider FBS: ", FBS_mostCommonDivider)
print("Most common divider FMY: ", FMY_mostCommonDivider)

print("Most common combined: ", (mostCommonDivider(FBS_distances + FMY_distances)))

# now that we have some possible block lenghts we can split the text and analyze which letters are the most
# common for every position (exp: 1: V / O, 2: X / Z, ...)

# for that we define functions that does exactly that

def mostFrequentLetters(string, blocksize):
    result = []

    for i in range(blocksize):
        letters = string[i::blocksize]

        counts = {}
        for letter in letters:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        if len(sorted_counts) >= 2:
            result.append((sorted_counts[0][0], sorted_counts[1][0]))
        elif len(sorted_counts) == 1:
            result.append((sorted_counts[0][0], None))
        else:
            result.append((None, None))

    return result

# now we print the most common letters for every postition for the block size of six

print(mostFrequentLetters(example2Encoded, 6))

# with this we can guess some keys that could 

print(example2Encoded)
print(decodeVigenereCipher(example2Encoded,"KRYPTO"))


