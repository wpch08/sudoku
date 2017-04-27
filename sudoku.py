# -*- coding:utf-8 -*- 

def candidate(x):
	y = map(list, zip(*x))
	res = [[i, j, [t for t in range(1,10)\
		if t not in x[i]\
		if t not in y[j]\
		if t not in x[i/3*3][j/3*3:j/3*3+3]\
		if t not in x[i/3*3+1][j/3*3:j/3*3+3]\
		if t not in x[i/3*3+2][j/3*3:j/3*3+3]]]\
		for i in range(9)\
		for j in range(9)\
		if x[i][j] == 0]
	return res

def solve(x):
	res = candidate(x)
	if len(res) == 0:
		return 0
	for ele in res:
		if len(ele[2]) == 0:
			return -1
	for i in res[0][2]:
		x[res[0][0]][res[0][1]] = i
		flag = solve(x)
		if flag == -1:
			x[res[0][0]][res[0][1]] = 0
			continue
		if flag == 0:
			return 0
	return -1

num = [[0,0,0,0,2,0,0,0,0],
	[0,9,5,4,0,0,0,1,0],
	[4,0,0,0,0,0,0,0,0],
	[0,0,0,0,3,8,9,0,0],
	[6,8,0,0,5,0,4,0,0],
	[0,0,0,9,0,7,0,0,0],
	[0,4,6,0,0,0,1,0,0],
	[3,0,0,1,0,0,0,2,0],
	[5,0,0,0,0,0,0,0,3]]
"""
num = [[4,5,0,9,0,8,0,0,0],
	[0,0,0,4,0,0,0,5,0],
	[0,1,6,5,0,0,4,9,0],
	[0,0,5,2,0,4,0,0,6],
	[0,0,0,6,0,5,0,2,9],
	[2,6,3,0,9,0,5,4,0],
	[0,0,0,3,5,9,0,0,4],
	[6,0,0,1,0,0,9,3,5],
	[5,3,9,0,4,6,2,1,0]]
"""	
solve(num)
for i in num:
	for j in i:
		print j,
	print
#print num

#print num[0][0:2]
