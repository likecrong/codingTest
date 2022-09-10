
# 3052

mlist = []
for i in range(10):
	mlist.append(int(input())%42)

mlist  = list(set(mlist)) #중복제거
print(len(mlist))