import random

n = 10
number_list = []
while n > 0:
    x = random.randint(1, 100)
    n -= 1
    number_list.append(x)
print("随机数列表为:", number_list)
x = 101
for k in number_list:
    if x > k:
        x = k
print("随机数列表中最小的值为:", x)
