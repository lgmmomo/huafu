import random

i = 0
f = open(r'D:\pythoncode\huafu\domnumber.txt', 'w+')

while i < 10000000:
  y = int(random.randint(2**63, 2**64-1))
  print(y)
  print(len(bin(y))-2)
  f.write(str(y) + "\n")
  f.flush()
  i = i + 1

# li = []
# with open(r'D:\pythoncode\huafu\domnumber.txt', 'r') as op:
#   for line in op:
#     lin = int(line)
#     li.append(line.strip())
# print(li)

# lis = sorted(li)
# print(lis)
#
# i = 0
# f = open(r'D:\pythoncode\huafu\domnumber.txt', 'w+')
# while i < 100:
#   m = li[i]
#   f.write(str(m) + "\n")
#   f.flush()
#   i = i + 1
