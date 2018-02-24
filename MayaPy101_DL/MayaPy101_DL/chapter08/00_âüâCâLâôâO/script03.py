#def mirrorGeometry(node, across=1, merge=True, softEdge=True, threshold=0.001):
	shapes = cmds.listRelatives(node, s=True, pa=True)
	if not shapes:
		return False
	
	if cmds.objectType(shapes[0]) != 'mesh':
		return False
	
	shape = shapes[0]
