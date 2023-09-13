def is_palindrome(word):
    word = word.lower()

    for i in range( (len(word)//2) ):
        if word[i] != word[len(word)-1-i]:
            return False

    return True

print(is_palindrome('racecar'))