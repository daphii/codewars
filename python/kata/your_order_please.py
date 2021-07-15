
def order(sentence):

    if sentence == '':
        return ''

    words = sentence.split(' ')
    ordered = ['' for word in words]

    for word in words:
        for i in word:
            try:
                idx = int(i) - 1
                ordered[idx] = word
            except:
                continue

    return ' '.join(ordered)

print(order("4of Fo1r pe6ople g3ood th5e the2"))

