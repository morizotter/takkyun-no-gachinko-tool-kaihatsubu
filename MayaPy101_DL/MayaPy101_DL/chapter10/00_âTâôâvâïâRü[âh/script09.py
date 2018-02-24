# カレントのレンダーレイヤーの取得
renderLayer = cmds.editRenderLayerGlobals(q=True, currentRenderLayer=True)

# レンダーレイヤーのメンバーを取得する
members = cmds.editRenderLayerMembers(renderLayer, q=True)

# １つずつ処理する
for node in members:
	pass
