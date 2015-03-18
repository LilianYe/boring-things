# 1012
import string
num_list = raw_input().split()
num_list = num_list[1:]
num_list = map(int, num_list)
A = [0, 0, 0, 0, 0]
Aflag = [False, False, False, False, False]
flag = 1
A4num = 0
for num in num_list:
    if(num % 5 == 0 ):
        if(num % 2 == 0):
            Aflag[0] = True
            A[0] = A[0] + num
    elif(num % 5 == 1):
        Aflag[1] = True
        A[1] = A[1] + num * flag
        flag = -flag
    elif(num % 5 == 2):
        Aflag[2] = True
        A[2] = A[2] + 1
    elif(num % 5 == 3):
        Aflag[3] = True
        A[3] = A[3] + num
        A4num = A4num + 1
    elif(num % 5 == 4):
        Aflag[4] = True
        if(num > A[4]):
            A[4] = num

if(Aflag[3]):
    A[3] = A[3] * 1.0 / A4num
    A[3] = round(A[3], 1)
for i in range(0, 5):
    if(not Aflag[i]):
        A[i] = 'N'

A = map(str, A)
print ' '.join(A)