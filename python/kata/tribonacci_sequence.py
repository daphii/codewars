def tribonacci(signature, n):
    
    out = signature
    sum_idx = 0

    for i in range(n-3):
        out.append(sum(out[sum_idx:sum_idx+3]))
        sum_idx += 1

    return out[:n]


print(tribonacci([300, 200, 100], 2))