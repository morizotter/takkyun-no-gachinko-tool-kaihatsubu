def average(*args): #指定された引数は、args にまとめられる
	sum = 0.0
	for arg in args:
		sum += arg
	return sum / len(args) if len(args)!=0 else 0
	
average(1, 2, 3, 4, 5, 6, 7, 8, 9)
# >> 5.0
