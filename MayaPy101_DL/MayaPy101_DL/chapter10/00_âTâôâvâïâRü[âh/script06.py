# 全てのノードを取得する
nodes = cmds.ls(allPaths=True)

#1つずつ処理する
for node in nodes:
	
	#applySmoothというアトリビュートがノードにあるか確認する
	if cmds.attributeQuery('applySmooth', exists=True, node=node):
	
		#アトリビュートがある場合の処理
		pass
