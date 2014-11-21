#! /usr/bin/env python

import numpy as np # short name saves typing
import matplotlib.pyplot as plt

x = [0, 3.2, 4.5, 0.9]
y = [4, 0.3, 5, 4.1]

plt.plot(x, y, "r^")
plt.axis([-0.5, 5, 0, 4.5])
plt.show()