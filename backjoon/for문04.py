
# 11022

num = int(input())
mlist = []

for i in range(num):
	mlist.append([int(x) for x in input().split()])

for i in range(len(mlist)):
	print("Case #",end ="")
	print(i+1,end ="")
	print(": ",end ="")
	print(mlist[i][0],end = "")
	print(" + ",end = "")
	print(mlist[i][1],end = "")
	print(" = ",end ="")
	print(mlist[i][0] + mlist[i][1])