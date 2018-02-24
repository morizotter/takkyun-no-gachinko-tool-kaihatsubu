#	else:
#		direction = 2
#		index = 1
		
	kwargs = {}
	if merge:
		kwargs['mm']=True
		kwargs['mt']=threshold
	else:
		kwargs['mm']=False
		
	cmds.polyMirrorFace(shape, ws=True, d=direction, p=pivot[0:3], **kwargs)
