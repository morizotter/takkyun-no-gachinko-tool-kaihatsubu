from myTool.lib import qt
from PySide import QtGui, QtCore
window = QtGui.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)

mainLayout = QtGui.QVBoxLayout(window)

# ページのコントロール
pageCtrl = QtGui.QComboBox(window)
pageCtrl.addItem('Page1')
pageCtrl.addItem('Page2')
mainLayout.addWidget(pageCtrl)

stackedLayout = QtGui.QStackedLayout()
mainLayout.addLayout(stackedLayout)

# ページ1のWidget
page1 = QtGui.QWidget(window)
layout = QtGui.QHBoxLayout(page1)
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(QtGui.QPushButton('Page1A'))
layout.addWidget(QtGui.QPushButton('Page1B'))
layout.addWidget(QtGui.QPushButton('Page1C'))
stackedLayout.addWidget(page1)

# ページ2のWidget
page2 = QtGui.QWidget(window)
layout = QtGui.QVBoxLayout(page2)
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(QtGui.QPushButton('Page2A'))
layout.addWidget(QtGui.QPushButton('Page2B'))
layout.addWidget(QtGui.QPushButton('Page2C'))
stackedLayout.addWidget(page2)

# ページのコントローラーと、QStackedLayoutのページ変更をリンク
pageCtrl.activated[int].connect(stackedLayout.setCurrentIndex)
window.show()
