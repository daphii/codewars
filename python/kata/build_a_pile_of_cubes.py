def find_nb(m):

    v, n = 0, 0

    while v < m:
        n += 1
        nv = n ** 3
        v += nv
    
    return n if v == m else -1



print(find_nb(26825883955641))