from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)

layout = QtGui.QVBoxLayout(window)

# ページのコントロール
pageCtrl = QtGui.QComboBox(window)
pageCtrl.addItem('Page1')
pageCtrl.addItem('Page2')
layout.addWidget(pageCtrl)

stacked = QtGui.QStackedWidget()
layout.addWidget(stacked)

# ページ1のWidget
page1 = QtGui.QWidget(window)
layout = QtGui.QHBoxLayout(page1)
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(QtGui.QPushButton('Page1A'))
layout.addWidget(QtGui.QPushButton('Page1B'))
layout.addWidget(QtGui.QPushButton('Page1C'))
stacked.addWidget(page1)

# ページ2のWidget
page2 = QtGui.QWidget(window)
layout = QtGui.QVBoxLayout(page2)
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(QtGui.QPushButton('Page2A'))
layout.addWidget(QtGui.QPushButton('Page2B'))
layout.addWidget(QtGui.QPushButton('Page2C'))
stacked.addWidget(page2)

# ページのコントローラーと、QStackedLayoutのページ変更をリンク
pageCtrl.activated[int].connect(stacked.setCurrentIndex)
window.show()
