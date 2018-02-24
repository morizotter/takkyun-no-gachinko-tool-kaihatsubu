from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QTabWidget(window)
layout.addWidget(widget)

# Nurbus
page1 = QtGui.QWidget(window)
layout = QtGui.QHBoxLayout(page1)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/sphere.png'), '')
	)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/cube.png'), '')
	)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/cylinder.png'), '')
	)
widget.addTab(page1, 'Nurbus')

# Polygon
page2 = QtGui.QWidget(window)
layout = QtGui.QHBoxLayout(page2)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/polySphere.png'), '')
	)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/polyCube.png'), '')
	)
layout.addWidget(
	QtGui.QPushButton(QtGui.QIcon(':/polyCylinder.png'), '')
	)
widget.addTab(page2, 'Polygon')

window.show()
