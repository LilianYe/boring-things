str_list = raw_input().split()
str_list.reverse()
print_str = ''
for stri in str_list:
    print_str = print_str + ' ' + stri

print_str = print_str[1:]
print print_str

