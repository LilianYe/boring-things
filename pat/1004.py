import copy
import string
str_num = raw_input()
str_num = string.atoi(str_num)
str_list = []
for i in range(1, str_num + 1):
    temp = raw_input().split()
    str_list.append(temp)

score_list = []
for stri in str_list:
    score_list.append(int(stri[2]))

score_ori = copy.copy(score_list)
score_list.sort()
max_id = score_ori.index(score_list[-1])
min_id = score_ori.index(score_list[0])
print str_list[max_id][0] + ' ' + str_list[max_id][1]
print str_list[min_id][0] + ' ' + str_list[min_id][1]