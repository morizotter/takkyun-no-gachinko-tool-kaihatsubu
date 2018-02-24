def createPolygonCube(**kwargs): 	# 引数が、kwargsにまとめられる
	return cmds.polyCube(**kwargs)	# Mayaコマンドにそのまま引数を渡す
	
createPolygonCube(name='cube_geo')
