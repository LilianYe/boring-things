# a1058
num_list = raw_input().split()
a = map(int, num_list[0].split('.'))
b = map(int, num_list[1].split('.'))
c = [0, 0, 0]
jin = 0
c[2] = a[2] + b[2]
if c[2] > 29:
    c[2] -= 29
    jin = 1
c[1] = a[1] + b[1] + jin
jin = 0
if c[1] > 17:
    c[1] -= 17
    jin = 1
c[0] = a[0] + b[0] + jin
c = map(str, c)
print '.'.join(c)