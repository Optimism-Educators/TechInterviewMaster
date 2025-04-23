# Author: <Antim Pal>
# Date: <22/04/2025>
# Description: Remove Punctuation from a String
# Input: String
# Output: String without Punctuation
# Note: Punctuation is defined as any character that is not a letter or a digit.
# Input
string = input("Enter a string: ")

# Process
string1 = string.replace("!","")
string2 = string.replace(".","")
string3 = string.replace(",","")
string4 = string.replace(";","")
string5 = string.replace(":","")
string6 = string.replace("-","")
string7 = string.replace("?","")
string8 = string.replace("(","")
string9 = string.replace(")","")
string10 = string.replace(" ","")

# Output
print("String without punctuation: ", string)
print("String without punctuation: ", end="")
print(string)
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)
print(string6)
print(string7)
print(string8)
print(string9)
print(string10)
