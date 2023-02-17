num = 2
sum = 0

while (num<=100):
    is_prime = True
    i = 2
    while(i<num):
        if(num%i == 0):
            is_prime = False
        i = i + 1
    if is_prime == True:
        sum = sum + num
    num = num +1
    
print(sum)
        