# 2675 문자열 반복

t = int(input())

s = ""
for i in range(t):
	mlist = [x for x in input().split()] #문자열 한 줄을 공백문자로 나누기
	for k in mlist[1]:
		for j in range(int(mlist[0])):
			s += k		
			
	print(s)
	s = ""	
