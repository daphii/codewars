def duplicate_encode(word):
    
    low = word.lower()
    out_str = ''
    
    for i in low:
        if low.count(i) > 1:
            out_str += ')'
        else:
            out_str += '('

    return(out_str)

print(duplicate_encode('@RbRnkuvQ@m)@Pw!cy dTmcTdmyxJm'))


