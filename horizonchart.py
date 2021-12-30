import numpy as np
from matplotlib.pyplot import *

def layer(y,height):
    neg=0.0;pos=0.0
    if y>0:
        if y-height>=0:
            pos=height
            y-= pos
        else :
            pos = y
    elif y<0:
        if y+height<=0:
            neg=height
            y += neg
        else :
            neg = -y
    return pos,neg

def horizonPlot(x,y,height=50.0,colors=['CornflowerBlue','DarkGreen']):
    alpha = .10
    vlayer = np.vectorize(layer)
    while (y != 0).any():
        l = vlayer(y,height)
        y -= l[0];y += l[1]
        fill_between(x,0,l[0],color=colors[0], alpha=alpha)
        fill_between(x,height-l[1],height,color=colors[1], alpha=alpha)

def main():
    x = np.linspace(0, np.pi*4, 137)
    y = (2*np.random.normal(size=137) + x**2)
    xx = np.hstack([-1*x[::-1], x])
    yy = np.hstack([-1*y[::-1], y])
    horizonPlot(xx,yy)
    horizonPlot(xx, yy,"red")
    horizonPlot(xx, yy)
    show()
main()