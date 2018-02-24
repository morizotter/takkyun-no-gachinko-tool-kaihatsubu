for dst in selection[1:]:
	shapes = cmds.listRelatives(dst, s=True, pa=True, type='mesh')
	if not shapes:
		continue

	dstSkinCluster = cmds.listConnections(	shapes[0]+'.inMesh',
											s=True,
											d=False
											)									
	if not dstSkinCluster:
		dstSkinCluster = cmds.skinCluster(
							dst,
							influences,
							omi=maintainMaxInfluences,
							mi=maxInfluences,
							dr=dropoffRate,
							sm=skinningMethod,
							nw=normalizeWeights,
							tsb=True,
							)
	dstSkinCluster = dstSkinCluster[0]
	
	# ここから追加
	cmds.copySkinWeights(
				ss=srcSkinCluster,
				ds=dstSkinCluster,
				surfaceAssociation='closestPoint',
				influenceAssociation=['name', 'closestJoint', 'oneToOne'],
				normalize=True,
				noMirror=True
				)
				
	print 'Transfar skin weight ' + selection[0] + '>' + dst