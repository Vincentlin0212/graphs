#! /usr/bin/env python

from special_input import int_input
import numpy as np # short name saves typing
import matplotlib.pyplot as plt
import random

times = int_input("How many time should I row? >")
add = random.randint(1, 100)
times += add
print("I know you want to throw {} times".format(times))
datas = []

for i in range(times):
	data = random.randint(1, 6)
	datas.append(data)

plt.hist(datas, bins = 6)
plt.xlim([1, 6])

plt.title("Results of rolling {} dice".format(times))

plt.xlabel("Dice Number")
plt.ylabel("Number of Rolls")

plt.show()