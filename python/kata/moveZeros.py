import timeit

testArrays = [[1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9], [0, 0], [0]]

def move_zeros(array):
    moveArray = []
    zeroArray = []
    for i in array:
        if i != 0:
            moveArray.append(i)
        else:
            zeroArray.append(i)
    return moveArray + zeroArray

for array in testArrays:
    move_zeros(array)