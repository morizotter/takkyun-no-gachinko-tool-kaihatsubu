from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QComboBox(window)
widget.addItem('Sphere')
widget.addItem('Cube')
widget.addItem('Cylinder')
layout.addWidget(widget)

window.show()