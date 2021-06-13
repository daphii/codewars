# All even coordinate sums are a dark square, and odd light.

def bishop_and_pawn(bishop, pawn):

    bloc = [ord(bishop[0]), int(bishop[1])]
    ploc = [ord(pawn[0]), int(pawn[1])]

    return abs(bloc[0]-ploc[0]) == abs(bloc[1]-ploc[1])

    

print(bishop_and_pawn('h1', 'h3'))