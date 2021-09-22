testThrow = [[1,2,10], [3], [1,2,4,7,5,8], [9,8,5], [10,6,9]]

def bowling_pins(throws):
    pins = ["I" for i in range(10)]
    pinPlacement = "{6} {7} {8} {9}\n {3} {4} {5} \n  {1} {2}  \n   {0}   "
    for throw in throws:
        pins[throw-1] = " "
    return pinPlacement.format(*pins)

for throw in testThrow:
    print("Throw -> {}\n-------\n{}".format(throw, bowling_pins(throw)))


