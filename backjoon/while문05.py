

# 10951 A+B-4

import sys

ans = []

while True:
	mlist = sys.stdin.readline().split()
	mlist = list(map(int, mlist))
	if not mlist :
		break
	ans.append(mlist[0] + mlist[1])
	mlist = []	
	
for i in ans:
	print (i)
