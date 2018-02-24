srcSkinCluster = cmds.listConnections(shapes[0]+'.inMesh', s=True, d=False)
if not srcSkinCluster:
	cmds.error('Select a node that has a skin cluster applied.')