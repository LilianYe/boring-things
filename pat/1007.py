import string
import math
num = string.atoi(raw_input())

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

primepair = 0
primelist = []
if num >= 5:
    for i in range(3, num + 1, 2):
        if(isPrime(i)):
            primelist.append(True)
        else:
            primelist.append(False)
    maxlen = len(primelist)
    for i in range(0, maxlen - 1):
        if(primelist[i] and primelist[i+1]):
            primepair += 1

print primepair