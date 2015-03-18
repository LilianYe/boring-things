# a1002
polya = map(float, raw_input().split())
polyb = map(float, raw_input().split())

nozeroa = int(polya[0])
polya = polya[1:]
nozerob = int(polyb[0])
polyb = polyb[1:]
polyab = []
j = 0
i = 0
while i < nozeroa  and j < nozerob:
    if polya[2*i] > polyb[2*j]:
        polyab.append(int(polya[2*i]))
        polyab.append(polya[2*i+1])
        i += 1
    elif polya[2*i] == polyb[2*j]:
        if polya[2*i+1] + polyb[2*j+1] != 0:
            polyab.append(int(polya[2*i]))
            polyab.append(round(polya[2*i+1]+polyb[2*j+1], 1))
            j += 1
            i += 1
    else:
        polyab.append(int(polyb[2*j]))
        polyab.append(polyb[2*j+1])
        j += 1
while i < nozeroa:
    polyab.append(int(polya[2*i]))
    polyab.append(polya[2*i+1])
    i += 1
while j < nozerob:
    polyab.append(int(polyb[2*j]))
    polyab.append(polyb[2*j+1])
    j += 1

nozeroab = len(polyab) / 2
polyab.insert(0, nozeroab)

print ' '.join(map(str, polyab))