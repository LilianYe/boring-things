# 1123 AC
s = raw_input()
N = len(s)
if N % 2 == 0:
    news = s[:N/2]
    if s[N/2-1] > s[N/2]:
        news = news + news[::-1]
else:
    news = s[:N/2+1]
    news = news + news[:-1][::-1]

print news



