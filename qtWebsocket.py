from PyQt5 import QtWebSockets, QtCore
import json

app = QtCore.QCoreApplication([])

url = QtCore.QUrl('wss://www.bitmex.com/realtime')

websocket = QtWebSockets.QWebSocket()


def get_message(msg):
    if 'version' in msg:
        websocket.sendTextMessage('{"op": "subscribe", "args": ["trade:XBTUSD"]}')
    else:
        print(json.loads(msg))


websocket.textMessageReceived.connect(get_message)

websocket.open(url)

app.instance().exec()



# Mesh grid
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# from scipy.interpolate import griddata
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# xyz = np.array(np.random.random((100, 3)))
# x = xyz[:, 0]
# y = xyz[:, 1]
# z = xyz[:, 2]
#
# df = pd.DataFrame({'x': x, 'y': y, 'z': z})
# x1 = np.linspace(df['x'].min(), df['x'].max(), len(df['x'].unique()))
# y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
#
# x2, y2 = np.meshgrid(x1, y1)
# z2 = griddata((df['x'], df['y']), df['z'], (x2, y2), method='cubic')
#
#
# ax.plot_surface(x2,y2,z2)
