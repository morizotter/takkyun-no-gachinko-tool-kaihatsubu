def main():
	nodes  = cmds.ls(sl=True, type='transform')
	if not nodes:
		OpenMaya.MGlobal.displayError('Select polygon to mirror geometry')
		return
	
	for node in nodes:
		mirrorGeometry(node)
	
	OpenMaya.MGlobal.displayInfo('Done') 
