#class StockerView(QtGui.QTreeView):
#	～中略～
#	def keyPressEvent(self, event):
		if event.matches(QtGui.QKeySequence.Copy):
			self.copyToClipboard()
		elif event.matches(QtGui.QKeySequence.Paste):
			self.pasteFromClipboard()
		else:
			super(StockerView, self).keyPressEvent(event)
