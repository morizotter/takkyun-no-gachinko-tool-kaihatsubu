# 演算子「+ 」を使用すると、複数のlist型tuple型を連結して１つにまとめることができます。
# ＜使用例＞
listA = ['pSphere', 'pCube']
listB = ['animCurveTL', 'animCurveTT']
listC = listA + listB
# >>['pSphere', 'pCube', 'animCurveTL', 'animCurveTT']

# また、リストの機能「extend」を使用すると、list型の末尾にlist型tuple型を追加できます。
# ＜使用例＞
listA = ['pSphere', 'pCube']
listB = ['animCurveTL', 'animCurveTT']
listA.extend(listB)
# >>['pSphere', 'pCube', 'animCurveTL', 'animCurveTT']

# 一方、dict型を連結する場合は、メソッド「update」を使用して行います。
# ＜使用例＞
dictA = {'node':'pSphere1'}
dictB = {'attr':'translateX'}
dictA.update(dictB)
# >> {'node': 'pSphere1', 'attr': 'translateX'}
