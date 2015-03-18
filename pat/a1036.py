# a1036
num = int(raw_input())
m_min = 101
f_max = -1
m_name = ''
m_id = ''
f_name = ''
f_id = ''
m = False
f = False
for i in range(0, num):
    record = raw_input().split()
    if record[1] == 'M':
        m = True
        if int(record[3]) < m_min:
            m_min = int(record[3])
            m_name = record[0]
            m_id = record[2]
    else:
        if int(record[3]) > f_max:
            f = True
            f_max = int(record[3])
            f_name = record[0]
            f_id = record[2]

if f and m:
    print f_name + ' ' + f_id
    print m_name + ' ' + m_id
    print str(f_max-m_min)
elif f:
    print f_name + ' ' + f_id
    print 'Absent'
    print 'NA'
else:
    print 'Absent'
    print m_name + ' ' + m_id
    print 'NA'