def okamelSim(c,e):
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


bsp3 = "PQHKBCD LRNZNTDUHKXHIHQYAZHLKQFKMCU CMHZGTQYAHZKUQZZHKPQHKULMPQHKVRZKFHLARPHZKMZPKLHYAZQBHZKMFKQZORCFNLQRZHZKNMUKVHCUYATMHUUHTLHZKLHELHZKIMKGHJQZZHZKPQHUHKQZORCFNLQRZHZKBRHZZHZKURJRATKPHCKVHCJHZPHLHKUYATMHUUHTKJQHKNMYAKPHCKRCQGQZNTLHELKUHQZKAHMLIMLNGHKXHIHQYAZHLKPHCKXHGCQOOKBCD LRNZNTDUHKNTTGHFHQZHCKPQHKNZNTDUHKVRZKBCD LRGCN AQUYAHZKVHCONACHZKFQLKPHFKIQHTKPQHUHKHZLJHPHCKIMKXCHYAHZKNTURKQACHKUYAMLIOMZBLQRZKNMOIMAHXHZKRPHCKQACHKUQYAHCAHQLKZNYAIMJHQUHZKMZPKIMKSMNZLQOQIQHCHZKBCD LRNZNTDUHKQULKPNFQLKPNUKGHGHZULMHYBKIMCKBCD LRGCN AQH"
e = [(' ', 'P'), ('A', 'H'), ('B', 'K'), ('C', 'R'), ('D', 'Y'), ('E', 'X'), ('F', 'M'), ('G', 'G'), ('H', 'E'), ('I', 'Z'), ('J', 'W'), ('K', ' '), ('L', 'T'), ('M', 'U'), ('N', 'A'), ('O', 'F'), ('P', 'D'), ('Q', 'I'), ('R', 'O'), ('S', 'Q'), ('T', 'L'), ('U', 'S'), ('V', 'V'), ('W', '.'), ('X', 'B'), ('Y', 'C'), ('Z', 'N')] 
okamelSim(bsp3,e)
