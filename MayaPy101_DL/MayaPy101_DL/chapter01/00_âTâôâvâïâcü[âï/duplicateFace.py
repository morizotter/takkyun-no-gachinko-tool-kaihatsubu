# -*- coding: utf-8 -*-
from maya import cmds

def duplicateFace(targetFaces):
	temp = targetFaces[0].split('.')	
	object = temp[0]	
	newNode = cmds.duplicate(object, rr=True)[0]
	keepFaces = []
	
	for targetFace in targetFaces:
		face = targetFace.split('.')[-1]
		face = newNode + '.' + targetFace.split('.')[-1]
		keepFaces.append(face)
		
	cmds.select(newNode+'.f[*]')
	cmds.select(keepFaces, d=True)
	deleteFaces = cmds.ls(sl=True)
	
	if deleteFaces:
		cmds.delete(deleteFaces)
		cmds.select(newNode)
	
	else:
		cmds.delete(newNode)
		

def main():
	selects = cmds.filterExpand(sm=34)
	if not selects:
		print u'フェイスを選択して実行してください'
		return False
	
	duplicateFace(selects)