#class KeyButton(QtGui.QWidget):
#	def __init__(self, *args, **kwargs):
#		super(KeyButton, self).__init__(*args, **kwargs)
#		
#		layout = QtGui.QHBoxLayout()
#		self.setLayout(layout)
#		
#		button = QtGui.QPushButton('Genga')
		button.clicked.connect(setGengaKeyframe)
#		layout.addWidget(button)
#		
#		button = QtGui.QPushButton('Douga')
		button.clicked.connect(setDougaKeyframe)
#		layout.addWidget(button)
