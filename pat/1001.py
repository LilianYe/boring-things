import string
num = raw_input()
num = string.atoi(num)
step = 0
if(num > 0 and num < 1000):
  while (num != 1):
      if(num % 2 == 0):
          num = num / 2
      else:
          num = (3 * num + 1) / 2
      step += 1
  print step