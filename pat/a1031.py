# a1031
str_list = raw_input()
lenght = len(str_list)
height = (lenght + 2)/ 3
width = lenght - height * 2
blank = ''
for i in range(0, width):
    blank = blank + ' '
for i in range(0, height - 1):
    print str_list[i] + blank + str_list[-i-1]
print str_list[height-1:height+width+1]