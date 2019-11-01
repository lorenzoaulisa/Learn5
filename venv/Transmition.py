# Transposition Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi__ertmsaeta__att_rnmtti_sasce_esg_htiwn_otasi

#  Program will define a method of scambling encrytion
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

# Program will define a method of scambling decryption
def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

# Program will finish defining the scramble encryption method so that it will be available for use
def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt(msg)
    print("The encrypted message is:", cipherText)

# write a stripSpaces(text) function here
# Program define a way to strip all spaces from a text
def stripSpaces(text):
    strippedText = ""
    for ch in text:
        if ch != " ":
            strippedText += ch
    return strippedText
# Completed

# Write a caesarEncrypt(plainText, shift)
# Program will create a method to simulate the caesar encrypt
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
def ceaserEncrypt(word, shift):
    cipherText = ""
    for ch in word:
        if ch == " ":
            cipherText += " "
        else:
            index = alphabet.find(ch)
            nextIndex = (index + shift) % 53
            cipherText += alphabet[nextIndex]
    return cipherText
# Completed


# Write a caesarDecrypt(cipherText, shift)
# Program will create a method to simulate the caesar decrypt
def ceaserDecrypt(word, shift):
    cipherText = ""
    for ch in word:
        if ch == " ":
            cipherText += " "
        else:
            index = alphabet.find(ch)
            nextIndex = (index - shift);
            if nextIndex < 0:
                nextIndex = 53 + nextIndex
            cipherText += alphabet[nextIndex]
    return cipherText
# Completed
