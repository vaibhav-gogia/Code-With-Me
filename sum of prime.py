# Start by taking an input of the number from the user

num = 99
sum = 0
# Initializing the sum to 0
for x in range(2, num + 1):
# Using for loop starting from 2 as it is the first prime number.
    i = 1
    for i in range(2, x):
        if (int(x % i) == 0):
            i = x
            break;
#Only if the number is a prime number, continue to add it.
    if i is not x:
        sum = sum + x
print("\nThe sum of prime numbers in python from 1 to ", num, " is :", sum)
