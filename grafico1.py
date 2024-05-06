import matplotlib.pyplot as plt
import math
i = 0
x = []
while i < 10:
    x.append(i)
    i = i + 0.1

y = []
i = 0
while i < len(x):
    y.append(math.sin(x[i]))
    i = i + 1
print(y)
plt.plot(x,y)
plt.show()

