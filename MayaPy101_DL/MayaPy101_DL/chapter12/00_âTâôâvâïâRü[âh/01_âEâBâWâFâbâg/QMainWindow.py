from myTool.lib import qt
from PySide import QtGui, QtCore

window = QtGui.QMainWindow(qt.getMayaWindow())

# メニュー
menuBar = window.menuBar()
menu = menuBar.addMenu('File')
openAct = menu.addAction(QtGui.QIcon(':/fileOpen.png'), 'Open')
saveAct = menu.addAction(QtGui.QIcon(':/fileSave.png'), 'Save')

# ツールバー
toolBar = window.addToolBar('Main')
toolBar.addAction(openAct)
toolBar.addAction(saveAct)

# ステータスバー
statusBar = window.statusBar()
statusBar.showMessage('Ready...')

window.show()
