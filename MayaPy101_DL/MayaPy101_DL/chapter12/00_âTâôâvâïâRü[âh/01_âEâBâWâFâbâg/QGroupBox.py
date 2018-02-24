from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

groupBox = QtGui.QGroupBox('Common Settings', window)
layout.addWidget(groupBox)

formLayout = QtGui.QFormLayout(groupBox)
formLayout.addRow('Amount', QtGui.QDoubleSpinBox(groupBox))
formLayout.addRow('Twist', QtGui.QDoubleSpinBox(groupBox))
groupBox.setLayout(formLayout)
window.show()
