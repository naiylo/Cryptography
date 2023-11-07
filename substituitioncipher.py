# Substituition-Cipher

# easy example that you could solve with Brute-Force

dictionary = e = [(' ', 'P'), ('A', 'H'), ('B', 'K'), ('C', 'R'), ('D', 'Y'), ('E', 'X'), ('F', 'M'), ('G', 'G'), ('H', 'E'), ('I', 'Z'), ('J', 'W'), ('K', ' '), ('L', 'T'), ('M', 'U'), ('N', 'A'), ('O', 'F'), ('P', 'D'), ('Q', 'I'), ('R', 'O'), ('S', 'Q'), ('T', 'L'), ('U', 'S'), ('V', 'V'), ('W', '.'), ('X', 'B'), ('Y', 'C'), ('Z', 'N')] 
example1Decoded = ""
example1Encoded = "bsp3 = "PQHKBCD LRNZNTDUHKXHIHQYAZHLKQFKMCU CMHZGTQYAHZKUQZZHKPQHKULMPQHKVRZKFHLARPHZKMZPKLHYAZQBHZKMFKQZORCFNLQRZHZKNMUKVHCUYATMHUUHTLHZKLHELHZKIMKGHJQZZHZKPQHUHKQZORCFNLQRZHZKBRHZZHZKURJRATKPHCKVHCJHZPHLHKUYATMHUUHTKJQHKNMYAKPHCKRCQGQZNTLHELKUHQZKAHMLIMLNGHKXHIHQYAZHLKPHCKXHGCQOOKBCD LRNZNTDUHKNTTGHFHQZHCKPQHKNZNTDUHKVRZKBCD LRGCN AQUYAHZKVHCONACHZKFQLKPHFKIQHTKPQHUHKHZLJHPHCKIMKXCHYAHZKNTURKQACHKUYAMLIOMZBLQRZKNMOIMAHXHZKRPHCKQACHKUQYAHCAHQLKZNYAIMJHQUHZKMZPKIMKSMNZLQOQIQHCHZKBCD LRNZNTDUHKQULKPNFQLKPNUKGHGHZULMHYBKIMCKBCD LRGCN AQH"

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

# decoding function

def decodeSubstituitionCipher(c,e):
    result = ""
    for i in c:
        bekannt = False
        for j in e:
            if j[0] == i:
                result = result + j[1]
                bekannt = True
        if bekannt == False:
            result = result + "."
    print(result)
    print(e)

    
okamelSim(bsp3,e)
