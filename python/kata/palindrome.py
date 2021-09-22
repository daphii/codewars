testWords = ["tattarrattat", "tartrates", "racecar", "banana", "Girafarig", "desserts", "Madam"]

# checks if a given string (case insensitive) is a palindrome. Returns Boolean
def is_palindrome(inputString):
    inputString = inputString.lower()   
    return inputString == inputString[::-1]

for word in testWords:
    print(is_palindrome(word))