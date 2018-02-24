from maya import cmds
def main(baseName, start):
	selectionNodes = cmds.ls(sl=True)
	for node in selectionNodes:
		cmds.rename(node, baseName+str(start))
		start += 1

# 実行
main('bg', 100)

# または
main(baseName='bg', start=100)
