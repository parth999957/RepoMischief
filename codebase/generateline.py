from matplotlib import pyplot as plt
from matplotlib import lines
import numpy as np

# bottom = np.array([0, 0])
# top = np.array([1, 1])
p1 = (7,8,9)

p2 = (90, 70, 500)

# plt.plot((p1[0], p2[0]), (p1[1], p2[1]), color='red', linewidth=3)

#create a 3d plot
ax = plt.axes(projection='3d')
ax.plot3D((p1[0], p2[0]), (p1[1], p2[1]), (p1[2], p2[2]), color='red', linewidth=3)

# plt.plot((0,100,),(100,0), color='red', linewidth=3)

# plt.plot()
# line = lines.Line2D(bottom, top, color='red', linewidth=3)

# plt.figure()
# plt.gca().add_line(line)

plt.show()