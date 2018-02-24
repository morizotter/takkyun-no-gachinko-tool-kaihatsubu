#class OptionWidget(QtGui.QWidget):
#	～略～
#	def __setItems(self, nodes, attrs):
#		if not nodes or not attrs:
#			return
#		
		for node in nodes:
			for attr in attrs:
				value = cmds.getAttr('%s.%s' % (node, attr))
				self.__model.appendItem(node, attr, value)
