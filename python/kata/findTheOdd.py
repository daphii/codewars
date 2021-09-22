testLists = [[7], [0], [1,1,2], [0,1,0,1,0], [1,2,2,3,3,3,4,3,3,3,2,2,1]]

def find_it(inputList):
    for i in inputList:
        if inputList.count(i) % 2 == 1:
            return i

for item in testLists:
    print(find_it(item))