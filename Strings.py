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
if 'j' in greeting:
    print('yes')
else:
    print("no")
    
my_string2 = '   Hello World    '
print(my_string2)
print(my_string2.strip())

print(my_string2.upper())
print(my_string2.lower())

print(my_string2.startswith('   Hello'))
print(my_string2.find('o'))