#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
For testing rapid updates of ScatterPlotItem under various conditions.

(Scatter plots are still rather slow to draw; expect about 20fps)
"""

## Add path to library (just for examples; you do not need this)

from pyqtgraph.Qt import QtGui, QtCore, USE_PYSIDE, USE_PYQT5
import pyqtgraph.opengl as gl

import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time

# QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
# mw = QtGui.QMainWindow()
# mw.resize(800,800)

from testGroupTemplate import Ui_MainWindow

win = QtGui.QMainWindow()
win.setWindowTitle('pyqtgraph example: VideoSpeedTest')
ui = Ui_MainWindow()
ui.setupUi(win)
win.show()

l = ui.verticalLayout
w = gl.GLViewWidget()
l.addWidget(w)
print(w)

w.opts['distance'] = 20
w.show()
w.setWindowTitle('pyqtgraph example: GLViewWidget')

ax = gl.GLAxisItem()
ax.setSize(5, 5, 5)
w.addItem(ax)

b = gl.GLBoxItem()
w.addItem(b)

ax2 = gl.GLAxisItem()
ax2.setParentItem(b)

b.translate(1, 1, 1)

w2 = gl.GLViewWidget()
l.addWidget(w2)

w2.opts['distance'] = 200
w2.show()
w2.setWindowTitle('pyqtgraph example: GLVolumeItem')

# b = gl.GLBoxItem()
# w.addItem(b)
g = gl.GLGridItem()
g.scale(10, 10, 1)
w2.addItem(g)


## Hydrogen electron probability density
def psi(i, j, k, offset=(50, 50, 100)):
    x = i - offset[0]
    y = j - offset[1]
    z = k - offset[2]
    th = np.arctan2(z, (x ** 2 + y ** 2) ** 0.5)
    phi = np.arctan2(y, x)
    r = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    a0 = 2
    # ps = (1./81.) * (2./np.pi)**0.5 * (1./a0)**(3/2) * (6 - r/a0) * (r/a0) * np.exp(-r/(3*a0)) * np.cos(th)
    ps = (1. / 81.) * 1. / (6. * np.pi) ** 0.5 * (1. / a0) ** (3 / 2) * (r / a0) ** 2 * np.exp(-r / (3 * a0)) * (
                3 * np.cos(th) ** 2 - 1)

    return ps

    # return ((1./81.) * (1./np.pi)**0.5 * (1./a0)**(3/2) * (r/a0)**2 * (r/a0) * np.exp(-r/(3*a0)) * np.sin(th) * np.cos(th) * np.exp(2 * 1j * phi))**2


data = np.fromfunction(psi, (100, 100, 200))
positive = np.log(np.clip(data, 0, data.max()) ** 2)
negative = np.log(np.clip(-data, 0, -data.min()) ** 2)

d2 = np.empty(data.shape + (4,), dtype=np.ubyte)
d2[..., 0] = positive * (255. / positive.max())
d2[..., 1] = negative * (255. / negative.max())
d2[..., 2] = d2[..., 1]
d2[..., 3] = d2[..., 0] * 0.3 + d2[..., 1] * 0.3
d2[..., 3] = (d2[..., 3].astype(float) / 255.) ** 2 * 255

d2[:, 0, 0] = [255, 0, 0, 100]
d2[0, :, 0] = [0, 255, 0, 100]
d2[0, 0, :] = [0, 0, 255, 100]

v = gl.GLVolumeItem(d2)
v.translate(-50, -50, -100)
w2.addItem(v)

ax = gl.GLAxisItem()
w2.addItem(ax)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
