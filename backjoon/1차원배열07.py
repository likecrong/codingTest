
# 8958

t = int(input())

count = 0
total = 0
mlist = []
for i in range(t):
	result = input()
	for j in result:
		if j == "O": 
			count += 1
			total += count #1씩 증가한 수를 더해줌
		else:
			count = 0 #연속 아니면 처음부터 다시
	mlist.append(total)
	total = 0
	count = 0

for i in mlist:
	print(i)	
