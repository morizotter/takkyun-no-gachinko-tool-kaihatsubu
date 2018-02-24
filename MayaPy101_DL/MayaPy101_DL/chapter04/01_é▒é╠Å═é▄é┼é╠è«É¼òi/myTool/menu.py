# -*- coding: utf-8 -*-
from maya import cmds

def main():
	cmds.menu(l='My Tool', p='MayaWindow', to=True)
	cmds.menuItem(l='Rigging', to=True, sm=True, aob=True)
	cmds.menuItem(	l='Transfar Weight',
					c='from myTool.rigging import transfarWeight;transfarWeight.main()'
					)