# Program will define a method to translate a letter into a character code
def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       # not found
        print("error:", letter, "is not in the alphabet")
    return idx

# Program will define a method to translate a character code back into a letter
def indexToLetter(idx):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    letter = ''
    if idx >= len(alphabet):
        print("error:", idx, "is too large")
    elif idx < 0:
        print("error:", idx, "is too small")
    else:
        letter = alphabet[idx]
    return letter
