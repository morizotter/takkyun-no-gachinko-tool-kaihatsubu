#選択された「ノード」を処理の対象とする
transforms = cmds.ls(sl=True)

#選択された「ジョイント」を処理の対象とする
#typeを併用することで、フィルタリングできる
lamberts = cmds.ls(sl=True, type='joint')

#選択された「ポリゴンフェイス」を処理の対象とする
#選択されたコンポーネントはlsでも取得できますが、filterExpandを使うことで
#関係のないものをフィルターできます。
faces = cmds.filterExpand(selectionMask=34)

#filterExpandは、同名ノードがある場合に処理がエラーしやすくなるので
#fullPathを併用することをオススメします。
faces = cmds.filterExpand(selectionMask=34, fullPath=True)

#lsでコンポーネントを取得する場合は、
#polygon.f[0:10]などと、連続したIDはまとめられてしまうので
#flattenを使用して、展開することをオススメします。
faces = cmds.ls(sl=True, fl=True)
