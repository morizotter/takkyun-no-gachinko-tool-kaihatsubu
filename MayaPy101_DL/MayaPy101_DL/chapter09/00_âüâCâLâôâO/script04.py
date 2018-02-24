class StockerView(QtGui.QTreeView):	
	def __init__(self, *args, **kwargs):
		super(StockerView, self).__init__(*args, **kwargs)
		self.setSelectionMode(QtGui.QTreeView.ExtendedSelection)
		self.setAlternatingRowColors(True)
		self.setRootIsDecorated(False)
