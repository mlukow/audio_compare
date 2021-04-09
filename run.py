#!bin/python3

import matplotlib.pyplot as plt
import numpy as np

config = "vocal_removal"
file_1 = "{}.before".format(config)
file_2 = "{}.after".format(config)

f = open(file_1, "rb")
y1 = np.fromfile(f, dtype=np.int16)# / 32767 to normalise
f.close()

f = open(file_2, "rb")
y2 = np.fromfile(f, dtype=np.int16)# / 32767 to normalise
f.close()

len_y1 = len(y1)
len_y2 = len(y2)
if len_y1 < len_y2:
    y2 = y2[:len_y1]
    len_x = len_y1
else:
    y1 = y1[:len_y2]
    len_x = len_y2

start = 60000

y1 = y1[start:100000]
offset = 2048
y2 = y2[start+offset:100000+offset]

n = int(len(y1) / 2)

x = [a for a in range(start, start + n)]

plt.plot(x, y1[:2*n:2], label=file_1)
plt.plot(x, y2[:2*n:2], label=file_2)
plt.legend()
plt.show()
