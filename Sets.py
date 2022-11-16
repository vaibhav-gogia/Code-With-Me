#does not allow duplicates

myset = {1, 2, 3, 1, 3}   
print(myset)

myset2 = set()
 
myset2.add(1)
myset2.add(2)
 
myset2.remove(2)
 
print(myset2)

if 1 in myset2:
    print("yes")
    
#unions & interesection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

#difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2 ,3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)  

setA.update(setB)
print(setA)