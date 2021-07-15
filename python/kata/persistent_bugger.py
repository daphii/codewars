def persistence(n):

    steps = 0
    while len(str(n)) > 1:
        product = 1
        factors = [int(i) for i in str(n)]
        for i in factors:    
            product = product * i
        steps += 1
        n = product

    return steps

print(persistence(39))
        
    


