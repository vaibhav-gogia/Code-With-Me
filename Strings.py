#Strings: ordered, immutable, text representation
my_string = "Hello World"
print(my_string)
print("\n")

char = my_string[0]
print(char)
print("\n")

#slicing
substring = my_string[1:5]
print(substring)
print("\n")

substring2 = my_string[::2]
print(substring2)
print("\n")

#reversing a string
reverseString = my_string[::-1]
print("the reversed string is:")
print(reverseString)
print("\n")

#concatenate
newString = my_string + " " + reverseString
print("the concatenated string is:")
print(newString)
print("\n")

greeting = "Hello"
for i in greeting:
    print(i)
print("\n")
if 'e' in greeting:
    print('yes')
else:
    print("no")