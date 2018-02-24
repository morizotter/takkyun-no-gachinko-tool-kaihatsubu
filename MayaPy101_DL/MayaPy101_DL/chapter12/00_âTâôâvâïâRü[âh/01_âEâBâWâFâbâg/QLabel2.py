from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QLabel(window)
widget.setPixmap(QtGui.QPixmap(':/polyCube.png'))
layout.addWidget(widget)

window.show()
