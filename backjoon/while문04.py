# 10952 A+B-5

import sys

ans = []

while True:
	mlist = sys.stdin.readline().split()
	mlist = list(map(int, mlist))
	if(mlist[0] == 0 and mlist[1] == 0) :
		break
	ans.append(mlist[0] + mlist[1])	
	
for i in ans:
	print (i)