
# 1546

t = int(input())

mlist = [int(x) for x in input().split()]
max_num = max(mlist)

result = 0
for i in mlist:
	result += i/max_num*100

print(result/t)