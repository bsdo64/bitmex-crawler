# -*- coding: utf-8 -*-
"""
This example demonstrates the use of GLSurfacePlotItem.
"""


## Add path to library (just for examples; you do not need this)
import initExample

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pandas as pd
from scipy.interpolate import griddata
import numpy as np

## Create a GL View widget to display data
app = QtGui.QApplication([])
import pyqtgraph.opengl as gl

w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=50)

## Add a grid to the view
g = gl.GLGridItem()
g.scale(2,2,1)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

xyz = np.array(np.random.random((50, 3)))
x = xyz[:, 0]
y = xyz[:, 1]
z = xyz[:, 2]

df = pd.DataFrame({'x': x, 'y': y, 'z': z})
x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))

x2, y2 = np.meshgrid(x1, y1)
z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='linear')

p1 = gl.GLSurfacePlotItem(z=z2, shader='shaded', color=(0.5, 0.5, 1, 1))
w.addItem(p1)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
