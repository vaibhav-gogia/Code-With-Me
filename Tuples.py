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
print(my_tuple)
print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('l'))

my_list = list(my_tuple)
print(my_list)


#slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)

c = a[::2]
print(c)

#reverse tuple using slicing
d = a[::-1]
print(d)

#unpacking a tuple

name, age, city = mytuple
print(name)
print(age)
print(city)