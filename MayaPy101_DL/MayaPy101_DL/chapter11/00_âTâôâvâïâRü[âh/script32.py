# 可読性が下がる例
z = [[x * y for y in range(1, 4)] for x in range(1,4)]
# >>[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
