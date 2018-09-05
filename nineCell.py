"""
3x3のセルに1〜9の数字をいれて縦横ななめの
合計を同じにする
"""

cells = []
result = []

"""
1〜9までの数字を全パターン作成し、
チェックして条件に合致していたら出力する
"""
def make_pattern(n, m = 0):
	if n == m: 
		check15(cells)
		#result.append(cells)
	else:
		for x in range(1, n + 1):
			if x in cells: continue
			cells.append(x)
			make_pattern(n, m + 1)
			cells.pop()
			
"""
9セルのうち、横3行の合計が15ならOKとして
出力する
"""
def check15(ninecell):
	if sum(ninecell[:3]) == 15:
		if sum(ninecell[3:6]) == 15:
			if sum(ninecell[6:]) == 15:
				if sum(ninecell[::3]) == 15:
					if sum(ninecell[1::3]) == 15:
						if sum(ninecell[2::3]) == 15:
							if ninecell[0] + ninecell[4] + ninecell[8] == 15:
								if ninecell[2] + ninecell[4] + ninecell[6] == 15:
									prtNinecell(ninecell)				
									result.append(ninecell)
	
"""
9マスの内容に出力
"""						
def prtNinecell(ninecell):
	print('-----')
	print(str(ninecell[0]) + '|' + str(ninecell[1]) + '|' + str(ninecell[2]))
	print('-----')
	print(str(ninecell[3]) + '|' + str(ninecell[4]) + '|' + str(ninecell[5]))
	print('-----')
	print(str(ninecell[6]) + '|' + str(ninecell[7]) + '|' + str(ninecell[8]))
	print('-----')	
								
if __name__ == '__main__':
	make_pattern(9)
	print('パターン数は ' + str(len(result)) + ' です。')
