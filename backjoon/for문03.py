# 11021

num = int(input())
ans = []
for i in range(num):
	mlist = [int(x) for x in input().split()]
	ans.append(mlist[0] + mlist[1])

for i in range(len(ans)):
	print("Case #",end ="")
	print(i+1,end ="")
	print(": ",end ="")
	print(ans[i])