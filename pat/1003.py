import string
str_num = raw_input()
str_num = string.atoi(str_num)
str_list = []
for i in range(1, str_num + 1):
    str_list.append(raw_input())


for stri in str_list:
    i = 0
    right = True
    if stri[i] == 'A':
        a = stri[i]
        tt = a
        i += 1
        if ( i > len(stri) - 1):
            right = False
            stri = 'PAT'
            i = 0
        while(stri[i] != 'P'):
            if(stri[i] == tt):
                a += tt
            else:
                right = False
                stri = 'PAT'
                i = 0
                break
            i += 1
            if( i > len(stri) - 3):
                right = False
                stri = 'PAT'
                i = 0
                
        i += 1 
        if i > len(stri) - 2:
            right = False
            stri = 'PAT'
            i = 1
        b = ''
        while(stri[i] != 'T'):
            if(stri[i] != 'A'):
                right = False
                stri = 'PAT'
                i = 2
                break
            else:
                b += 'A'
            i += 1
            if( i > len(stri) - 1):
                right = False
                stri = 'PAT'
                i = 2
        if i < len(stri) - 1:
            i += 1
            c = ''
            while i < len(stri):
                if(stri[i] == tt):
                    c += tt
                else:
                    right = False
                    break
                i += 1
            if len(c) % len(a) != 0 or len(c) / len(a) != len(b):
                right = False
        else:
            right = False

    elif stri[i] == 'P':
        i += 1
        if( i > len(stri) - 1 or stri[i] != 'A'):
            right = False
            stri = 'PAT'
            i = 1
        while(i < len(stri) and stri[i] == 'A'):
            i += 1
        if i != len(stri) - 1 or stri[i] != 'T':
            right = False
    else:
        right = False
    if right:
        print 'YES'
    else:
        print 'NO'