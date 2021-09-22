testNums = [10, 21, 25, 34, 55, 78, 122, 315, 1450, 7896]

def solution(number):
    multiplesSum = 0
    for i in range(number):
        if i % 3 == 0 & i % 5 == 0:
            multiplesSum += i
        elif i % 5 == 0:
            multiplesSum += i
        elif i % 3 == 0:
            multiplesSum += i
    return multiplesSum

for num in testNums:
    print("{} -> {}".format(num, solution(num)))