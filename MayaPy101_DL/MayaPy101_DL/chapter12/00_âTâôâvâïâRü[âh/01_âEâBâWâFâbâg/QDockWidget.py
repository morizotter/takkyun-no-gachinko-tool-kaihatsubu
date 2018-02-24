from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QMainWindow(qt.getMayaWindow())
window.setCentralWidget(QtGui.QWidget())

dockA = QtGui.QDockWidget('DockA', window)
window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockA)

dockB = QtGui.QDockWidget('DockB', window)
window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockB)

dockC = QtGui.QDockWidget('DockC', window)
window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockC)

window.show()
