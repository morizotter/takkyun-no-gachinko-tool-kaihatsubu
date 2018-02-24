counter = 0			# グローバル変数

def countUp():
	global counter	# グローバル変数を関数で使うおまじない
	counter += 1	# グローバル変数の値を　+1　する
	
def countDown():
	global counter	# 同上
	counter -= 1	# グローバル変数の値を　-1　する
