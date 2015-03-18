import string
aa = raw_input().split()
N = int(aa[0])
M = int(aa[1])
num_list = raw_input().split()
map(int, num_list)

for i in range(0, (N - M)/2):
    temp = num_list[i]
    num_list[i] = num_list[N-M-1-i]
    num_list[N-M-1-i] = temp

for i in range(N-M, N-(M+1)/2):
    temp = num_list[i]
    num_list[i] = num_list[2*N-1-M-i]
    num_list[2*N-M-1-i] = temp
    
num_list.reverse()

map(str, num_list)
print ' '.join(num_list)