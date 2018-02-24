def curve_wrapper(*args, **kwargs):
	name = kwargs.pop('name', kwargs.pop('n', None))
	curve = cmds.curve(*args, **kwargs)
	if name:
		curve = cmds.rename(curve, name)
	return curve
