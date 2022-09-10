# 2577

x = int(input())
y = int(input())
z = int(input())

result = str(x*y*z)

mlist = [0,0,0,0,0,0,0,0,0,0]

for i in result:
	for j in range(10):
		if i == str(j):
			mlist[j] += 1

for i in mlist:
	print(i)	
