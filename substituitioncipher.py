# Substituition-Cipher

# easy example that you could solve with Brute-Force

dictionary = e = [(' ', 'P'), ('A', 'H'), ('B', 'K'), ('C', 'R'), ('D', 'Y'), ('E', 'X'), ('F', 'M'), ('G', 'G'), ('H', 'E'), ('I', 'Z'), ('J', 'W'), ('K', ' '), ('L', 'T'), ('M', 'U'), ('N', 'A'), ('O', 'F'), ('P', 'D'), ('Q', 'I'), ('R', 'O'), ('S', 'Q'), ('T', 'L'), ('U', 'S'), ('V', 'V'), ('W', '.'), ('X', 'B'), ('Y', 'C'), ('Z', 'N')] 
example1Decoded = "DIE KRYPTOANALYSE BEZEICHNET IM URSPRUENGLICHEN SINNE DIE STUDIE VON METHODEN UND TECHNIKEN UM INFORMATIONEN AUS VERSCHLUESSELTEN TEXTEN ZU GEWINNEN DIESE INFORMATIONEN KOENNEN SOWOHL DER VERWENDETE SCHLUESSEL WIE AUCH DER ORIGINALTEXT SEIN HEUTZUTAGE BEZEICHNET DER BEGRIFF KRYPTOANALYSE ALLGEMEINER DIE ANALYSE VON KRYPTOGRAPHISCHEN VERFAHREN MIT DEM ZIEL DIESE ENTWEDER ZU BRECHEN ALSO IHRE SCHUTZFUNKTION AUFZUHEBEN ODER IHRE SICHERHEIT NACHZUWEISEN UND ZU QUANTIFIZIEREN KRYPTOANALYSE IST DAMIT DAS GEGENSTUECK ZUR KRYPTOGRAPHIE"
example1Encoded = "PQHKBCD LRNZNTDUHKXHIHQYAZHLKQFKMCU CMHZGTQYAHZKUQZZHKPQHKULMPQHKVRZKFHLARPHZKMZPKLHYAZQBHZKMFKQZORCFNLQRZHZKNMUKVHCUYATMHUUHTLHZKLHELHZKIMKGHJQZZHZKPQHUHKQZORCFNLQRZHZKBRHZZHZKURJRATKPHCKVHCJHZPHLHKUYATMHUUHTKJQHKNMYAKPHCKRCQGQZNTLHELKUHQZKAHMLIMLNGHKXHIHQYAZHLKPHCKXHGCQOOKBCD LRNZNTDUHKNTTGHFHQZHCKPQHKNZNTDUHKVRZKBCD LRGCN AQUYAHZKVHCONACHZKFQLKPHFKIQHTKPQHUHKHZLJHPHCKIMKXCHYAHZKNTURKQACHKUYAMLIOMZBLQRZKNMOIMAHXHZKRPHCKQACHKUQYAHCAHQLKZNYAIMJHQUHZKMZPKIMKSMNZLQOQIQHCHZKBCD LRNZNTDUHKQULKPNFQLKPNUKGHGHZULMHYBKIMCKBCD LRGCN AQH"

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

def decodeSubstituitionCipher(string, dictionary):
    result = ""
    for i in string:
        bekannt = False
        # if the letter is in the dictionary it will be replaced
        for j in dictionary:
            if j[0] == i:
                result = result + j[1]
                bekannt = True
        # if the letter is not in the dictionary it will be replaced with a dot
        if bekannt == False:
            result = result + "."
    
    return result

# encoding function

def encodeSubstituitionCipher(string, dictionary):
    result = ""
    for i in string:
        bekannt = False
        for j in dictionary:
            if j[1] == i:
                result = result + j[0]
                bekannt = True
    
    return result

# some tests to see if everything works
print("\nStart of tests\n")
print("Example decoded with dictionary: " + decodeSubstituitionCipher(example1Encoded, dictionary) + "\n")
print("Example encoded with dictionary: " + encodeSubstituitionCipher(example1Decoded, dictionary) + "\n")

    
