# Transposition Cipher

# original: this_is_a_secret_message_that_I_want_to_transmit
# encrypted: hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

# Program will create and define a method to encrypt text
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
    cipherText = oddChars + ch
    return cipherText

def scramble2Decrypt(ciphertext):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText = evenChars[i]
        plainText = plainText = oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText