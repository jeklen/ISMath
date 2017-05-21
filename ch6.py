from random import randrange
t = 20

def getb(n):
    flag = False
    while(flag == False):
        b = randrange(3, n-2, 2)
        flag = True
        for i in range(3, b):
            if (b%i ==0 and n%i ==0):
                flag = False
                break
    return b

low = pow(2, 12) - pow(2, 5) - 1
high = pow(2, 12) + pow(2, 5) + 1
for n in range(low, high, 2):
    count = t
    while(count):
        b = getb(n)
        r = pow(b, n-1) % n
        if(r != 0):
            break
        count = count - 1

print(n)
