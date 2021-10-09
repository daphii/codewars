testLocations = ['a1', 'c2', 'D4', 'g6']

def chess_knight(cell):
    origin = (ord(cell[0].lower()) - 96, int(cell[1]))
    potentialMoves = []
    for i in range(1,3):
        x = i
        y = 2
        if x == 2:
            y = 1
        for j in range(2):
            for k in range(2):
                potentialMoves.append((origin[0] + x, origin[1] + y))
                y = y - (2 * y)
            x = x - (2 * x)
    return len([x for x in potentialMoves if 9 > x[0] > 0 and 9 > x[1] > 0])

""" for location in testLocations:
    print('validMoves = {}\n'.format(chess_knight(location))) """