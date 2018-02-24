listA = ['pSphere', 'pCube', 'pCylinder']
listA.sort()
# >> ['pCube', 'pCylinder', 'pSphere']

dataA = [
    ('pSphere', 'translate', (0, 0, 0)),
    ('pSphere', 'rotate', (0, 90, 0)),
    ('pSphere', 'scale', (1, 1, 1))
]
dataB = sorted(dataA, key=lambda dataA: dataA[1])
# >> [('pSphere', 'rotate', (0, 90, 0)), ('pSphere', 'scale', (1, 1, 1)), ('pSphere', 'translate', (0, 0, 0))]
