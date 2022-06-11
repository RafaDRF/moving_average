import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = []
y = [4.1590,4.1293,4.0841,4.0556,4.1071,4.0954,4.1104,4.1095,4.1097,4.1265,4.1807,4.1518,4.1643,4.1117,4.1293,4.0819,4.0346]

for i in range(len(y)):
    x.append(i)


plt.title("Line graph")
plt.plot(x, y, color="red")

plt.show()