from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)

layout = QtGui.QFormLayout(window)
layout.addRow('Label A', QtGui.QLineEdit())
layout.addRow('Label B', QtGui.QSlider(QtCore.Qt.Horizontal))
layout.addRow(QtGui.QPushButton('ButtonA'))
window.show()