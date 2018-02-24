from myTool.lib import qt
from PySide import QtGui, QtCore

# ファイルを開く
fileName = QtGui.QFileDialog.getOpenFileName(
				qt.getMayaWindow(),
				'Open Image',
				'./',
				'Image Files (*.png *.jpg *.bmp)'
				)

# ファイルの保存
fileName = QtGui.QFileDialog.getSaveFileName(
				qt.getMayaWindow(),
				'Save File',
				'untitled.png',
				'Image Files (*.png *.jpg *.bmp)'
				)