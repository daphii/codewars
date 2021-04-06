

def find_outlier(integers):

    odd = [i for i in integers if i % 2 == 1]
    even = [i for i in integers if i % 2 == 0]

    return odd[0] if len(odd) < len(even) else even[0]

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))