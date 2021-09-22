testNums = [16, 942, 132189, 493193]

def digital_root(number):
    checkNum = number
    while len(str(checkNum)) > 1:
        rootSum = 0
        for i in str(checkNum):
            rootSum += int(i)
        checkNum = rootSum
    return checkNum

for num in testNums:
    print("{} -> {}".format(num, digital_root(num)))