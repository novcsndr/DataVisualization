import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import colors

data = pd.read_csv("iris.csv")

a =data['petal_length'].head()

print(data)
plt.xlabel('Petal Length in cm')
plt.ylabel('Frequency')

N, bSins, patches = plt.hist(x=a, bins=4, color='#0504aa')

plt.grid(axis='y')

fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())


for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.show()