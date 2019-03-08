#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
t = np.linspace(0.0, 10.0, 1000)
s = np.sin(2*np.pi*t)

plt.plot(s)
plt.show




