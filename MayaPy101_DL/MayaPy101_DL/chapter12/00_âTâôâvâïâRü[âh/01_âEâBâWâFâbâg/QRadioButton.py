from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

widgetA = QtGui.QRadioButton('TypeA',window)
widgetA.setChecked(True)
layout.addWidget(widgetA)
widgetB = QtGui.QRadioButton('TypeB',window)
layout.addWidget(widgetB)

window.show()
