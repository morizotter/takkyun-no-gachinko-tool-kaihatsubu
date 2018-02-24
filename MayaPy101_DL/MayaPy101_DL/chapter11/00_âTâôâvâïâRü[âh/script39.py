from maya import cmds
def main(baseName, start=1):
	selectionNodes = cmds.ls(sl=True)
	for node in selectionNodes:
		cmds.rename(node, baseName+str(start))
		start += 1
	
	return start

result = main('bg')		# 変数「result」に結果が代入される
print result
