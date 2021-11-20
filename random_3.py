import matplotlib.pyplot as matlib
import numpy as np

x = np.linspace(-5, 5)
y = x ** 2

matlib.title("y = x*x", fontdict={'family': "SimHei", 'size': 20})
matlib.xlabel("X", fontdict={'family': "SimHei", 'size': 20})
matlib.ylabel("Y", fontdict={'family': "SimHei", 'size': 20})
matlib.plot(x, y)
matlib.show()
