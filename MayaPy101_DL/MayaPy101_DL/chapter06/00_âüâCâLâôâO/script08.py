	try:
		temp = filename.split('.')
		format = temp[-1]
		image.writeToFile(filename, format)
	except:
		return False

	return True
