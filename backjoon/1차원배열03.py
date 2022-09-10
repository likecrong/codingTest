# 2920

mlist = [int(x) for x in input().split()]

incount = 0
decount = 0
for i in range(0,8):
	if i+1 == mlist[i]:
		incount += 1
	if i+1 == mlist[7-i]:
		decount += 1  

if incount == 8:
	print("ascending")
elif decount == 8:
	print("descending")
else :
	print("mixed")