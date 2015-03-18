# a1008
num_list = map(int, raw_input().split())
num = num_list[0]
num_list = num_list[1:]
total_time = 5 * num + num_list[0] * 6 
for i in range(0, num-1):
    if num_list[i+1] > num_list[i]:
        total_time += (num_list[i+1] - num_list[i]) * 6
    else:
        total_time += (num_list[i] - num_list[i+1]) * 4
    
print total_time