#		self.__scrollWidget = QtGui.QScrollArea(self)
#		self.__scrollWidget.setWidgetResizable(True)
#		self.__scrollWidget.setFocusPolicy(QtCore.Qt.NoFocus)
#		self.__scrollWidget.setMinimumHeight(1)
#		mainLayout.addWidget(self.__scrollWidget, 0, 0, 1, 3)
#
		self.__actionBtn = QtGui.QPushButton(self)		# 左
		self.__actionBtn.setText('Apply and Close')
		self.__actionBtn.clicked.connect(self. action)
		mainLayout.addWidget(self.__actionBtn, 1, 0)
		
		applyBtn = QtGui.QPushButton(self)			# 中
		applyBtn.setText('Apply')
		applyBtn.clicked.connect(self. apply)
		mainLayout.addWidget(applyBtn, 1, 1)
		
		closeBtn = QtGui.QPushButton(self)			# 右
		closeBtn.setText('Close')
		closeBtn.clicked.connect(self. close)
		mainLayout.addWidget(closeBtn, 1, 2)
