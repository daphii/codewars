testNums = [9119, 4321, 56765, 122, 27, 823]

def square_digits(inputNumber):
    output = ""
    for i in str(inputNumber):
        output += str(int(i) ** 2)
    return int(output)

for num in testNums:
    print(square_digits(num))