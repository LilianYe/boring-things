import string
str_num = raw_input()
str_num = string.atoi(str_num)
num_list = raw_input().split()
num_list = map(int, num_list)

cover_set_list = []
for num in num_list:
    cover_set = {1}
    while num not in cover_set:
        cover_set.add(num)
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num + 1) / 2
    cover_set_list.append(cover_set)

for cover_set in cover_set_list:
    cover_set.remove(1)

notcover = []
for i in range(0, str_num):
    for j in range(i+1, str_num):
        if(num_list[i] in cover_set_list[i] & cover_set_list[j]):
            break
        elif j == str_num -1:
            notcover.append(i)

notcovernum = []
for num in notcover:
    notcovernum.append(num_list[num])

notcovernum.sort()
notcovernum.reverse()

outstring = ''
for num in notcovernum:
    outstring = outstring + ' ' + str(num)

outstring = outstring[1:]
print outstring 