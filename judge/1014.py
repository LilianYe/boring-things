# 1014 AC
a = int(raw_input())
if a == 0:
    print 10
elif a == 1:
    print 1
else:
    t2 = 0
    while a % 2 == 0:
        t2 += 1
        a = a / 2

    t3 = 0
    while a % 3 == 0:
        t3 += 1
        a = a / 3

    t5 = 0
    while a % 5 == 0:
        t5 += 1
        a = a / 5

    t7 = 0
    while a % 7 == 0:
        t7 += 1
        a = a / 7

    t9 = t3 / 2
    t3 = t3 % 2
    t8 = t2 / 3
    t2 = t2 % 3
    if t2 == 0:
        result = '3'*t3+ '5'*t5 +'7'*t7+'8'*t8+'9'*t9
    elif t2 == 1 and t3 == 0:
        result = '2' + '5'*t5 +'7'*t7+'8'*t8+'9'*t9
    elif t2 == 1 and t3 == 1:
        result = '5'*t5 + '6'+'7'*t7+'8'*t8+'9'*t9
    elif t2 == 2 and t3 == 0:
        result = '4' +  '5'*t5 +'7'*t7+'8'*t8+'9'*t9
    else:
        result = '2'+ '5'*t5 +'6'+'7'*t7+'8'*t8+'9'*t9

    if a != 1:
        print -1
    else:
        print result