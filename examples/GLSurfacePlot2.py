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
gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)
w.addItem(gy)
gz = gl.GLGridItem()
gz.setSize(100, 100, 100)
gz.translate(0, 0, -10)
w.addItem(gz)

df = pd.read_csv('../test.csv', header=None)
x = np.arange(df.shape[1]-1)
y = np.arange(df.shape[0])
z = df.iloc[:,1:]

p1 = gl.GLSurfacePlotItem(x=x, y=y, z=z.transpose(), shader='shaded', color=(0.5, 0.5, 1, 1))
p1.translate(0, 0, -9000)
scale = 1/10
p1.scale(scale, scale, scale/100, local=False)
w.addItem(p1)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
