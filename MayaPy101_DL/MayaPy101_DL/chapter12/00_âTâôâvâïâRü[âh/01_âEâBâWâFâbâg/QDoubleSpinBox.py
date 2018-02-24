from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widget = QtGui.QDoubleSpinBox(window)
widget.setRange(-10, 10)
widget.setValue(3.14)
layout.addWidget(widget)

window.show()