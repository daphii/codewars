testNums = [3, 5, 7, 9, 11]

import math

def x(n):
    midpoint = math.ceil(n / 2)
    patternDict = {}
    for i in range(n):
        patternDict[i+1] = ['□' for x in range(n)]
        patternDict[i+1][i] = '■'
        patternDict[i+1][-(i+1)] = '■'
    output = ''
    for key in patternDict.keys():
        if output == '':
            output += "".join(patternDict[key])
        else:
            output += "\n" + "".join(patternDict[key])
    return output

def x2(n):
    artList = [['□' for x in range(n)] for x in range(n)]
    for i in range(n):
        artList[i][i] = '■'
        artList[i][-(i+1)] = '■'
    return "\n".join(''.join(art) for art in artList)

for num in testNums:
    print(x2(num))
    print()

