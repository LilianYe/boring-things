# a1011
num_list = []
prst = ''
total = 1
for i in range(0, 3):
    num = map(float, raw_input().split())
    if(num[0] > num[1]):
        if(num[0] > num[2]):
            num_list.append(num[0])
            prst = prst + 'W' + ' '
        else:
            num_list.append(num[2])
            prst = prst + 'L' + ' '
    else:
        if(num[1] > num[2]):
            num_list.append(num[1])
            prst = prst + 'T' + ' '
        else:
            num_list.append(num[2])
            prst = prst + 'L' + ' '

for i in range(0, 3):
    total *= num_list[i]
total = round((total * 0.65 - 1) * 2, 2)
prst = prst + str(total)
print prst