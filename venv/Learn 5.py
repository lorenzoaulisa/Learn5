# Strings
# Data that falls within " " marks

# Concatenation
# Put 2 or more strings together

firstName = "Gar -"
lastName = "Field"

fullName = firstName + " " + lastName

print(fullName)

# Repitition
# Repitition operator: *

print("Ooga"*3 + "chaka!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("life is but a dream")

rowYourBoat()

# Indexing

name = "What is Obama's last name?"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
# Slicing operator: :
# Slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)):
    print(name[0:i])