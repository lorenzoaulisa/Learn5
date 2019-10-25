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
    print("The letter y is in name")
else:
    print("The letter y is not in name")


# String Methods to investigate:
# Method        Use Example         Explanation
# center        aStr.center(w)      The center() method creates and returns a new string of a specific character
# ljust         aStr.ljust(w)       The ljust() method will left align the string, using a specified character to fill
# rjust         aStr.rjust(w)       The ljust() method will right align the string, using a specified character to fill
# upper         aStr.upper()        The upper() method returns the uppercased string from the given string.
#                                   It also converts all lowercase characters to uppercase.
# lower         aStr.lower()        The lower() method returns the lowercased string from the given string.
#                                   It converts all uppercase characters to lowercase.
# index         aStr.index(item)    Index() determines if string str occurs in string or in a substring of string if
#                                   starting index beg and ending index end are given. Very similar to find()
# rindex        aStr.rindex(item)   rindex() returns the last index where the substring str is found.
# find          aStr.find(item)     Same as index(), but doesn't have the exeption if sub is not found
# rfind         aStr.rfind(item)    rfind() returns the last index where the substring str is found, or -1 if no such
#                                   index is even present.
# replace       aStr.replace(old, new)  The replace() method returns a new string with some or all matches of a pattern
#                                   by something else.

# Be sure to include multiple examples of all of them in use
