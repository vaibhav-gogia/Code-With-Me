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

new_string = 'how are you doing'
new_list = new_string.split(" ")
print(new_list) 

#checking the time of the 2 weys below

hehe_list = ['a']*6
print(hehe_list)
from timeit import default_timer as timer

#bad python code
start = timer()
hehe_string = ''
for i in hehe_list:
    hehe_string += i
stop = timer()
print(stop-start)
print(hehe_string)

#good way
start = timer()
hehe2_string = ''.join(hehe_list)
stop = timer()
print(stop-start)
print(hehe2_string)


#formatting strings
# %, .format(), f-Strings

var = 3.1234567
var_string = "the variable is %f" % var
print(var_string)

var2_string = "the variable is {}".format(var)
print(var2_string)

#newest and the best way
var3_string = f"the variable is {var}"
print(var3_string)















