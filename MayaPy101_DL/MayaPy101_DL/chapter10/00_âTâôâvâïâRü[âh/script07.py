# set「exportAnimation」に登録されたメンバーを取得する
members = cmds.sets('exportAnimation', q=True)

# 選択されたノードが、set「exportAnimation」に登録されていれば処理する
# 選択されたノードの取得
selectedNodes = cmds.ls(sl=True)

# １つずつ処理する
for node in selectedNodes:
	
	# ノードが、setsのメンバーか確認する
	if cmds.sets(node, isMember='exportAnimation'):
	
		# 登録されていた場合の処理
		pass
