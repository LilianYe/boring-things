# a1035
num = int(raw_input())
change = []
for i in range(0, num):
    temp = raw_input().split()
    b = False
    newtemp = ''
    for j in range(0, len(temp[1])):
        if temp[1][j] == '1':
            newtemp += '@'
            b = True
        elif temp[1][j] == '0':
            newtemp += '%'
            b = True
        elif temp[1][j] == 'l':
            newtemp += 'L'
            b = True
        elif temp[1][j] == 'O':
            newtemp += 'o'
            b = True
        else:
            newtemp += temp[1][j]
    temp[1] = newtemp
    if b:
        change.append(temp)

if len(change) > 0:
    print str(len(change))
    for i in range(0, len(change)):
        print ' '.join(change[i])
else:
    if num == 1:
        print 'There is 1 account and no account is modified'
    else:
        print 'There are ' + str(num)+' accounts and no account is modified'