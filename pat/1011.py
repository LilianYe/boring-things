# 1011
num = int(raw_input())
num_list_list = [] 
for i in range(0, num):
    num_list = map(int, raw_input().split())
    if(num_list[0] + num_list[1] > num_list[2]):
        print "Case #" + str(i + 1) + ': true'
    else:
        print 'Case #' + str(i + 1) + ': false'