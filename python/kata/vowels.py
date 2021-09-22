vowelsList = "aeiou"
testWords = ["wrap", "position", "source", "panel", "power nap", "extreme", "frown", "Age", "troop", "unrest"]

def get_count(inputWord):
    vowelCount = 0
    for letter in inputWord.lower():
        if letter in vowelsList:
            vowelCount += 1
    return vowelCount

for word in testWords:
    print("There are {} vowels in {}".format(get_count(word), word))