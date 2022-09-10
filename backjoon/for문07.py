# 10871

import sys

NandX = sys.stdin.readline().split()
mlist = sys.stdin.readline().split()

# change for integer list
NandX = list(map(int, NandX))
mlist = list(map(int, mlist))

for i in range(NandX[0]) :
	if(NandX[1] > mlist[i]):
		print(mlist[i],end =" ")

