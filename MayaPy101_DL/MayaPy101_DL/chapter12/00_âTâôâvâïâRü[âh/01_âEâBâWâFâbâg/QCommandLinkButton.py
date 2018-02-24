from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QCommandLinkButton(
			'Cube',
			'Create a polygonal cube on the grid.',
			window)
widget.setIcon(QtGui.QIcon(':/polyCube.png'))
layout.addWidget(widget)

window.show()
