def order_weight(string):

    weights = string.split()

    for weight in weights:
        idx = 0
        w = weight
        for i in weight:
            idx += int(i)
        weights[weights.index(weight)] = (idx, w)
 
    return ' '.join([i[1] for i in sorted(weights)])



print(order_weight("103 123 4444 99 2000"))


