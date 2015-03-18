import string
num = string.atoi(raw_input())

a = num / 100
b = (num - a * 100) / 10
c = num % 10
outstr = ''
for i in range(0, a):
    outstr = outstr + 'B'
for i in range(0, b):
    outstr = outstr + 'S'
for i in range(1, c + 1):
    outstr = outstr + str(i)

print outstr