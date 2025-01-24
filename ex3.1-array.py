#! /usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


x = np.array([1,1,5,1])
y = np.array([1,5,1,1])

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
