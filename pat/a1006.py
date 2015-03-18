# a1006
num = int(raw_input())
record = []
min_sign_in_time = '23:59:59'
max_sign_out_time = '00:00:00'
min_sign_in_id = ''
max_sign_out_id = ''
for i in range(0, num):
    record = raw_input().split()
    if(record[1] < min_sign_in_time):
        min_sign_in_time = record[1]
        min_sign_in_id = record[0]
    if(record[2] > max_sign_out_time):
        max_sign_out_time = record[2]
        max_sign_out_id = record[0]

print min_sign_in_id + ' ' + max_sign_out_id