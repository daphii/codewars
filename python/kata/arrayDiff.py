testArrays = [[[1,2], [1]], [[1,2,2], [1]], [[1,2,2], [2]], [[1,2,3], [1, 2]], [[1,2,2], []]]

def array_diff(a, b):
    return [i for i in a if i not in b]

for pair in testArrays:
    print(array_diff(pair[0], pair[1]))