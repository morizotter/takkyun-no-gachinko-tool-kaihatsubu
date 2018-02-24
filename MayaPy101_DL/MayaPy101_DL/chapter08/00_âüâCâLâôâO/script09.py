#		centerVertices = []
#		for vertex in vertices:
#			pos = cmds.pointPosition(vertex, w=True)
#			if abs(pivot[index] - pos[index]) <= threshold:
#				centerVertices.append(vertex)

		centerEdges = []
		if centerVertices:
			centerEdges = cmds.polyListComponentConversion(
						centerVertices,
						fv=1, ff=1, fuv=1, fvf=1, te=1, internal=1
						)
		
		if centerEdges:
			cmds.polySoftEdge(centerEdges, a=180) 
