# a1025
location_num = int(raw_input())
local_num = []
infor = []
for i in range(0, location_num):
    local_num.append(int(raw_input()))
    local_infor = []
    for j in range(0, locan_num[i]):
        temp = map(int, raw_input().split())
        temp.append(i+1)
        local_infor.append(temp)