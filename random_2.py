import random
import numpy as np

number_list = [[], []]
n = 3
while n > 0:
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    number_list[0].append(x)
    number_list[1].append(y)
    n -= 1
print("随机的二维列表为：", number_list)
x = np.array(number_list[0])
y = np.array(number_list[1])
answer = [np.dot(x, y)]
print(answer)
