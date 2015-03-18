# a1019
num = map(int, raw_input().split())
number = num[0]
base = num[1]
num_list = []
while number != 0:
    num_list.append(str(number % base))
    number = number / base
num_list.reverse()
b = True
for i in range(0, len(num_list)/2):
    if num_list[i] != num_list[-i-1]:
        b = False
        break

if b:
    print 'Yes'
else:
    print 'No'
print ' '.join(num_list)