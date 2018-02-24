#def main():
#	cmds.menu(l='My Tool', p='MayaWindow', to=True)
#	cmds.menuItem(l='General', to=True, sm=True, aob=True)
#	cmds.menuItem(	l='Capture',
#					c='from myTool.general import capture;capture.main()'
#					)
	
	cmds.setParent('..', m=True)
	cmds.menuItem(l='Modeling', to=True, sm=True, aob=True)
	cmds.menuItem(	l='Mirror Geometry',
					c='from myTool.modeling import mirrorGeometry;mirrorGeometry.main()'
					)
	cmds.menuItem(	l='Mirror Geometry Option',
					ob=True,
					c='from myTool.modeling import mirrorGeometry;mirrorGeometry.option()'
					)
	
#	cmds.setParent('..', m=True)
#	cmds.menuItem(l='Animation', to=True, sm=True, aob=True)
#	cmds.menuItem(	l='Set Key',
#					c='from myTool.animation import setKey;setKey.main()'
#					)
