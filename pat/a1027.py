# a1027
num_list = map(int, raw_input().split())
prst = '#'
def numtostr(num):
    if num < 10:
        return str(num)
    if num == 10:
        return 'A'
    if num == 11:
        return 'B'
    if num == 12:
        return 'C'

for num in num_list:
    if num < 13:
        prst = prst + '0'
        prst = prst + numtostr(num)
    else:
        num1 = num / 13
        num2 = num % 13
        prst = prst + numtostr(num1) + numtostr(num2)
   
print prst