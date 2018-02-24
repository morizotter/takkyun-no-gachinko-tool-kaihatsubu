listA = ['pSphere']
listA.append('visible')
# >> ['pSphere', 'visible']

listA = ['pSphere']
listA.insert(0, 'visible')
# >> ['visible', 'pSphere']

dictA = {'obj':'pCube'}
dictA['attr'] = 'v'
# >> {'obj':'pCube', 'attr':'v' }

setA = set(['pSphere'])
setA.add('pCube')
# >> set(['pSphere', 'pCube'])
