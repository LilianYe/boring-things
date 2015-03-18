import string
num = raw_input()
num = string.atoi(num)
sum = 0
while(num != 0):
    sum += num % 10
    num = num / 10

newstring = ""
while(sum != 0):
    tp = sum % 10
    sum = sum / 10
    if tp == 0:
        tp = "ling"
    elif tp == 1:
        tp = 'yi'
    elif tp == 2:
        tp = 'er'
    elif tp == 3:
        tp = 'san'
    elif tp == 4:
        tp = 'si'
    elif tp == 5:
        tp = 'wu'
    elif tp == 6:
        tp = 'liu'
    elif tp == 7:
        tp = 'qi'
    elif tp == 8:
        tp = 'ba'
    else:
        tp = 'jiu'
    newstring = tp + ' ' + newstring

newstring = newstring[:-1]
print newstring