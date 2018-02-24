from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtGui.QHBoxLayout(window)

path  = r'C:\Program Files\Autodesk\Maya2016\devkit'
model = QtGui.QFileSystemModel()
model.setRootPath(path)

widget = QtGui.QTableView(window)
widget.setModel(model)
widget.setRootIndex(model.index(path))
layout.addWidget(widget)

widget.setModel(model)

window.show()
