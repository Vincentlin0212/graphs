#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)

plt.subplot(1, 2, 1)
PE = (10 - x) * 9.8
KE = 98 - PE

plt.plot(x, PE, "b", label = "Potential")
plt.plot(x, KE, "r", label = "Kinetic")
plt.legend(loc = "upper right")

plt.xlabel("Distance Fallen,$\\Delta$h (m)")
plt.ylabel("Energy, PE & KE, (j)")

plt.subplot(1, 2, 2)
t = np.sqrt(2 * x/9.8)
PE = (10 - x) * 9.8
KE = 98 - PE

plt.plot(t, PE, "b", label = "Potential")
plt.plot(t, KE, "r", label = "Kinetic")
plt.legend(loc = "upper right")

plt.xlabel("Time Fallen,$\\Delta$t (s)")
plt.ylabel("Energy, PE & KE, (j)")

plt.subplots_adjust(wspace = 1)

plt.suptitle("PE KE cool", fontsize = 30)

plt.show()