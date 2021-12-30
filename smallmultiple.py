import numpy as np
import matplotlib.pyplot as plt

bdg=[10.23,2.11,4.53,2.75,4.02]
prov=[11.11,2.02,6.62,3.1,3.86]
nas=[11.06,2.78,6.96,3.79,4.3]
year=[2008,2009,2010,2011,2012]
jak=[11.11,2.34,6.21,3.97,4.52]
a= len(year)
def make_plot(axs):
    box = dict(facecolor='yellow', pad=5, alpha=0.2)
    for i in range(a) :
        ax1 = axs[0, 0]
        ax1.set_title('Persentase Tingkat Inflasi 2008-2012')
        ax1.plot(year,bdg,"green")
        ax1.set_ylabel('Bandung', bbox=box)

        ax3 = axs[1, 0]
        ax3.plot(year, nas,"blue")
        ax3.set_ylabel('Nasional', bbox=box)

        ax2 = axs[0, 1]
        ax2.plot(year, jak,"orange")
        ax2.set_ylabel('Jakarta', bbox=box)

        ax4 = axs[1, 1]
        ax4.plot(year, prov,"red")
        ax4.set_ylabel('Jawa Barat', bbox=box)
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
# just align the last column of axes:
fig.align_ylabels(axs[:, 1])
plt.show()