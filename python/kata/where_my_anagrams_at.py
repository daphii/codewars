def anagrams(word, words):

    out = []
    letters = sorted([i for i in word])

    for test in words:
        tester = sorted([i for i in test])

        if letters == tester:
            out.append(test)

    return(out)

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))