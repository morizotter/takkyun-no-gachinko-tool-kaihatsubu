listA = ['pSphere', 'visible', True]
del listA[0]						# または、listA.pop(0)
# >> ['visible', True]

dictA = {'obj':'pCube', 'attr':'v', 'val':True}
del dictA['val']					# または、dictA.pop('val')
# >> {'obj': 'pCube', 'attr': 'v'}

listA = ['pSphere', 'visible', True]
listA.remove(True)
# >> ['pSphere', 'visible']

setA = set(['pSphere', 'pCube', 'pCylinder'])
setA.remove('pCube')
# >> set(['pSphere', 'pCylinder'])
