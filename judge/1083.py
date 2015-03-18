# 1083 AC
a = raw_input().split()
n = int(a[0])
k = len(a[1])

result = 1
if n % k == 0:
    t = k
    while t <= n:
        result *= t
        t += k
else:
    t = n % k
    while t <= n:
        result *= t
        t += k
print result