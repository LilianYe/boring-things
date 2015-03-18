# a1005
num = raw_input()
sum = 0
def numtostr(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    else:
        return 'nine'

for i in range(0, len(num)):
    sum += int(num[i])
prst = []
i = 1
while sum != 0:
    prst.append(numtostr(sum % 10))
    sum = sum / 10
    i += 1

prst.reverse()
print ' '.join(prst)