# a1001
num = map(int, raw_input().split())
nw = num[0] + num[1]
nw = str(nw)
flen = -1 * len(nw)
pst = ''
for i in range(-1, flen -1, -1):
    pst = nw[i] + pst
    if(i % 3 == 0 and i != flen and nw[i-1] != '-'):
        pst= ',' + pst
    
print pst 