# 1044 AC
a = int(raw_input())
if a == 2:
    print 10
elif a == 4:
    print 670
elif a == 6:
    print 55252
else:

    tt = 0
    sum_dict = {}
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    sum = i1 + i2 + i3 + i4
                    if sum in sum_dict.viewkeys():
                        sum_dict[sum] += 1
                    else:
                        sum_dict[sum] = 1

    for ff in sum_dict.viewkeys():
        tt += sum_dict[ff] * sum_dict[ff]
    print tt