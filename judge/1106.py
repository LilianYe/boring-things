# 1106 AC
N = int(raw_input())
fdict = {}
for i in range(N):
    fdict[i+1] = map(int, raw_input().split())[:-1]

this = set()
that = set()
all = range(1, N+1)
while all != []:
    i = all[0]
    tmp = []
    tmp1 = [i]
    this.add(i)
    all.remove(i)
    while tmp != [] or tmp1 != []:
        if tmp1 != []:
            for tt in tmp1:
                tmp1.remove(tt)
                for xx in fdict[tt]:
                    if (xx not in this) and (xx not in that):
                        that.add(xx)
                        tmp.append(xx)
                        all.remove(xx)

        if tmp != []:
            for tt in tmp:
                tmp.remove(tt)
                for xx in fdict[tt]:
                    if (xx not in this) and (xx not in that):
                        this.add(xx)
                        tmp1.append(xx)
                        all.remove(xx)

print len(this)
print " ".join(map(str,this))
