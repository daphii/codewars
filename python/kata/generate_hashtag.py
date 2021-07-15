
def generate_hashtag(s):
    
    if s == '' or len(s) > 140:
        return False

    return ''.join(['#',''.join(s.title().split())])

print(generate_hashtag('codewars is nice'))