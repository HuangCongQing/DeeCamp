# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 获取用户输入十进制数
print(10**12 + 1)
count = 0
for i in range(1, 10 ** 12 + 1):
    a = str(oct(i) % 10)
    b = str(oct(i**2) % 10)
    if a[-1] == b[-1]:
        conut = count + 1
    print(count)
print(count)
# x = pow(10, 12)
# count = 0
# for i in range(1, pow(10, 12) + 1):
#  a = str(oct(i))
#  if pow(i, 2) <= pow(10, 12):
#   b = str(oct(pow(i, 2)))
#   if a[-1] == b[-1]:
#    count += 1
# print(count)
