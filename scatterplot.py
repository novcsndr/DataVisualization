import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 60
g1 = (1.0, 2.0, 3.0,1.0,2.0, 6.0,7.0, 6.0, 7.0, 6.0, 8.0, 9.0, 10.0, 8.0, 9.0)
g2 = (-5.0, 5.0, -2.0,  2.0,  0.0, -5.0,  5.0, -2.0, 2.0, 0.0, -5.0, 5.0, -2.0, 2.0, 0.0)
g3 = (0.3 , 0.3, 0.5 , 0.5 , 0.7 , 0.5 , 0.5 , 0.3 , 0.3 , 0.7, 0.5 , 0.5 , 0.3 , 0.3 , 0.5)

data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("low", "medium", "high")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

for color, group in zip(colors, groups):
    # x, y = data
    ax.scatter(g1, g2, alpha=0.8, c=color, edgecolors='none', s=30, label=group)


for g1,g2,g3 in zip(g1,g2,g3):
    if(g3==0.3):
       ax.scatter(g1, g2, alpha=0.8, c="red", edgecolors='none', s=30)
    elif (g3 == 0.5):
       ax.scatter(g1, g2, alpha=0.8, c="green", edgecolors='none', s=30)
    elif (g3 == 0.7):
        ax.scatter(g1, g2, alpha=0.8, c="blue", edgecolors='none', s=30)


plt.title('Container Crane Controller Power')
plt.legend(loc=0)
plt.show()