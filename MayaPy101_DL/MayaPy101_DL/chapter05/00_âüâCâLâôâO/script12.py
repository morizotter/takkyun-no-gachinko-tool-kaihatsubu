def main():
	cmds.menu(l='My Tool', p='MayaWindow', to=True)
	cmds.menuItem(l='Rigging', to=True, sm=True, aob=True)
	cmds.menuItem(	l='Transfar Weight',
				c='from myTool.rigging import transfarWeight;transfarWeight.main()'
				)

	cmds.setParent('..', m=True)
	cmds.menuItem(l='Rendering', to=True, sm=True, aob=True)
	cmds.menuItem(	l='Fresnel Shader',
				c='from myTool.rendering import fresnelShader;fresnelShader.main()'
				)
