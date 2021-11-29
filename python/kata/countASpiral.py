from math import floor

testCases = [5, 7, 8, 9, 10, 1000, 123456]
testAnswers = [17, 31, 39, 49, 59, 500999, 7620815423]

def spiralSum(n):

    if n % 2 == 0:
        sum = -1
    else:
        sum = 0

    num = n * (n + 1)
    den = 2

    sum += num // den + n // 2

    return sum

for i in range(len(testCases)):
    print("Case: {} - Should equal: {} - currently equals {}".format(testCases[i], testAnswers[i], spiralSum(testCases[i])))

""" # 5 -> 25 -> 17 = 68%

# n-summation

def nSum(n):

    if n % 2 == 0:
        sum = -1
    else:
        sum = 0 

    num = n * (n + 1)
    den = 2
    sum += int(num / den) + floor(n / 2)

    return sum

for i in range(5,50):
    print("{} -> {} | {}".format(i, nSum(i), spiral_sum(i) == nSum(i))) """
