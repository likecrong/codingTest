#2562

numlist = []
for i in range(9):
	numlist.append(int(input()))
maxnum = max(numlist)
print(maxnum)
print(numlist.index(maxnum)+1)
