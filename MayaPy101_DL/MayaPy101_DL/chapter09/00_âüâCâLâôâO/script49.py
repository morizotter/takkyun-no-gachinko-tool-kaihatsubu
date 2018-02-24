#def main():
#	cmds.menu(l='My Tool', p='MayaWindow', to=True)
#	cmds.menuItem(l='General', to=True, sm=True, aob=True)
#	cmds.menuItem(	l='Capture',
#				c='from myTool.general import capture;capture.main()'
#				)
	cmds.menuItem(	l='Copy Attribute',
				c='from myTool.general import copyAttribute;copyAttribute.main()'
				)
