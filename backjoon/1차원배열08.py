
# 4344

t = int(input())

total = 0
count = 0
ansOfList = []

for i in range(t):
	mlist = [int(x) for x in input().split()]
	length = len(mlist)
	for j in range(length -1): #다음 원소부터 계산
		total += mlist[j+1]
	ex = total/mlist[0] #평균
		
	for j in range(length -1):
		if mlist[j+1] > ex:
			count += 1
	ans = count/(length -1) * 100 #맞은사람 비율계산
	
	ansOfList.append("%0.3f" % ans) #소수점 셋째자리
			
	mlist.clear()
	total = 0
	count = 0

for i in ansOfList:
	print(i + "%")
