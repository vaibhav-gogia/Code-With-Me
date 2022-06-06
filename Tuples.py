#Tuples
#allows duplicate elements but cannot be updated
mytuple = "Chris", 28, "Toronto"
print(mytuple) 
print(type(mytuple))

newtuple = tuple(["Max", 28, "Boston"])
print(newtuple)

item = mytuple[-1]
print(item) 

#mytuple[0] = "Tim" This is not possible

my_tuple = ('a','p','p','l','e')
print(len(my_tuple))
print(my_tuple.count('p'))