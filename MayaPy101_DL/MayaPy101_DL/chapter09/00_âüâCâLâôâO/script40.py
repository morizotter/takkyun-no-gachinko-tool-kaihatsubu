#	def pasteFromClipboard(self):
#		clipboard = QtGui.QApplication.clipboard()
		mimeData  = clipboard.mimeData()
		if not mimeData.hasFormat(StockerView.mimeType):
			return
