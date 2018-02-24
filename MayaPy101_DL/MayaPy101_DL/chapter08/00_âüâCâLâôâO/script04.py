#	if cmds.objectType(shapes[0]) != 'mesh':
#		return False
#	
#	shape = shapes[0]
	pivot = cmds.xform(node, q=True, ws=True, piv=True)