mydict = {"name": "Max", "age": 28, "city": "Toronto"}
print(mydict)

mydict2 = dict(name="Vaibhav", age=21, city="Toronto")
print(mydict2)

value = mydict["name"]
print(value)

#dictionary is mutable
mydict["email"] = "vbv@gmail.com"
print(mydict)

#deleting items
del mydict["name"]
mydict.pop("age")
print(mydict)

if "name" in mydict2:
    print(mydict2["name"])
    
try:
    print(mydict["lastname"])
except:
    print("Error")

#looping through a dict  
for key in mydict2:
    print(key)
    
for values in mydict2.values():
    print(values)
    
#copy a dict
mydict2_cpy = mydict2.copy()
print(mydict2_cpy)