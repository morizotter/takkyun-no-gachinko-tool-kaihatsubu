from maya import cmds
def main(baseName, start=1):
	selectionNodes = cmds.ls(sl=True)
	for node in selectionNodes:
		cmds.rename(node, baseName+str(start))
		start += 1

# 実行
main('bg')		# デフォルト値が使われ、1番から番号が振られる
main('bg', 100)	# デフォルト値で困る場合は指定する
