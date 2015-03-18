# a1042
import copy
repeat_num = int(raw_input())
num_list = map(int, raw_input().split())
ori_list = []
for i in range(1, 14):
    ori_list.append('S'+str(i))
for i in range(1, 14):
    ori_list.append('H'+str(i))
for i in range(1, 14):
    ori_list.append('C'+str(i))
for i in range(1, 14):
    ori_list.append('D'+str(i))
ori_list.append('J1')
ori_list.append('J2')
for i in range(0, repeat_num):
    temp_list = copy.copy(ori_list)
    for j in range(0, len(num_list)):
        temp_list[num_list[j]-1] = ori_list[j]
    ori_list = copy.copy(temp_list)
print ' '.join(ori_list)