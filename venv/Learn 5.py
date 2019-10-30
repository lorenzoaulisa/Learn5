# Strings
# Data that falls within " " marks

# Concatenation
# Put 2 or more strings together

# Program will define and print variables "firstName and lastName" to create to result of "Gar - Field"
firstName = "Gar -"
lastName = "Field"

fullName = firstName + " " + lastName

print(fullName)

# Repitition
# Repitition operator: *

# Program will print "OogaOogaOogachaka!"
print("Ooga"*3 + "chaka!")

# Program will define "row your boat" and print
# "Row, Row, Row, your boat
# Gently down the stream
# Merrily, Merrily, Merrily, Merrily,
# life is but a dream"
def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("life is but a dream")

rowYourBoat()

# Indexing

# Program will indexing to find/locate certain characters and character values
name = "What is Obama's last name?"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

# Program will print "What is Obama's last name". However, one character of the phrase takes of one space of code in
# the end result.
for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
# Slicing operator: :
# Slicing lets us make substrings

# Program will print parts of the phrase "What is Obama's last name" starting form one character value to when the
# instructions say to stop.
print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

# Program will create a loop and print many lines of coding. With every line, one character is added. The loop continues
# until the final result is, "What is Obama's last name?"
for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of strings

# Program will determine wether or not certain characters and smaller words/phrases are in the phrase " What is Obama's
# last name?"
print("Obama" in name)
print("LOP" not in name)

# Program will print one of the following base on wether or not y is in the phrase "What is Obama's last name?"
if "y" in name:
    print("The letter y is in \"" + name + "\"")
else:
    print("The letter y is not in \"" + name + "\"")


# String Methods to investigate:
# Method        Use Example         Explanation
# center        aStr.center(w)      The center() method creates and returns a new string of length w with aStr centered
print(name.center(len(name) + 20)  + "end")
print(name.center(len(name) + 16)  + "end")
print(name.center(len(name) + 12)  + "end")

# ljust         aStr.ljust(w)       The ljust()  method creates and returns a new string of length w with aStr left justified
print(name.ljust((len(name) + 20)) + "end")
print(name.ljust((len(name) + 16)) + "end")
print(name.ljust((len(name) + 12)) + "end")

# rjust         aStr.rjust(w)       The rjust() method creates and returns a new string of length w with aStr right justified
print(name.rjust((len(name) + 20)) + "end")
print(name.rjust((len(name) + 16)) + "end")
print(name.rjust((len(name) + 12)) + "end")

# upper         aStr.upper()        The upper() method creates and returns the uppercase string from the given string.
name1 = name.upper()
print(name1)
print(name1.lower())

# lower         aStr.lower()        The lower() method creates and returns the lowercase string from the given string..
name2 = name.lower()
print(name2)
print(name2.upper())

# index         aStr.index(item)    The index() method determines if string item, occurs in aStr or in a portion of aStr 
#                                   if starting index beg and ending index end are given aStr.index(item, beg, end). 
#                                   the method return the index where the item starts
#                                   This method is same as find(), but raises an exception if item is not found.
print(name.index("Obama")) 
print(name.index("Obama",5,15)) 
#print(name.index("Obama",0,10))    # This generates an exception

# rindex        aStr.rindex(item)   The rindex() method is the same as index(item) but it returns the index where the 
#                                   string item is last found.
print(name.index("a")) 
print(name.rindex("a")) 
#print(name.rindex("y"))             # This generates an exception


# find          aStr.find(item)     Same as index(), but doesn't have the exception if item is not found
print(name.find("Obama"))           #Same as name.index("Obama")
print(name.find("Obama",0,10))      #This does not generates an exception, it returns "-1"

# rfind         aStr.rfind(item)    Same as rindex(), but does not generate an exception if item is not found
print(name.find("a"))               #Same as name.rindex("a")
print(name.rfind("y"))              #This does not generates an exception, it returns "-1"

# replace       aStr.replace(old, new)  The replace() method returns a new string with some or all matches of a pattern
#                                   by something else.
print(name.replace("Obama", "Trump"))
print(name.replace("last", "first"))

# Character Functions

print(ord('A'))

print(ord('B'))

print(chr(104))

print(chr(97+13))

print(str(12548))

print(ord('5'))

# testing functions from mapper.py

from mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))

from Transmition import *

# Testing scramble code encrypt
print("Scramble test:")
encrypt = scramble2Encrypt("WHAT IS OBAMAS LAST NAME YOU STUPID GOOGLE MACHINE")
print(encrypt)
# Testing scramble code decrypt
decrypt = scramble2Decrypt(encrypt)
print(decrypt + "\n")

print("Ceaser upper case test:")
# Testing Ceaser upper case code encrypt
encrypt = ceaserEncrypt(decrypt, 3)
print(encrypt)
# Testing Ceaser upper case code decrypt
decrypt = ceaserDecrypt(encrypt,3)
print(decrypt+ "\n")

# Testing Ceaser lower case code encrypt
print("Ceaser lower case test:")
encrypt = ceaserEncrypt(decrypt.lower(), 5)
print(encrypt)
# Testing Ceaser lower case code decrypt
decrypt = ceaserDecrypt(encrypt,5)
print(decrypt+ "\n")

# Testing strip space code
print("Strip space test:")
print(stripSpaces(decrypt)+ "\n")
