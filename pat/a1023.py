# a1023
num = raw_input()
num1 = int(num)
num2 = num1 * 2
num2 = str(num2)
b = True
if len(num) != len(num2):
    b = False
else:
    n1 = []
    n2 = []
    for i in range(0, len(num)):
        n1.append(num[i])
        n2.append(num2[i])
    for i in range(0, len(num)):
        if n2[i] in n1:
            n1.remove(n2[i])
        else:
            b = False
            break

if b:
    print 'Yes'
else:
    print 'No'
print num2