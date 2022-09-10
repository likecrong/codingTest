# 1157 단어공부 

s = input()

mlist = [0 for x in range(26)]
count=0 # 최대 값 같은 게 있는 지 카운트 하는 변수

for i in s:
	x = ord(i)
	if x >= 97:
		x = x - 32

	mlist[x-65] += 1

m = max(mlist)

for i in mlist :
	if i == m:
		count += 1
if count >= 2:
	print("?")
else: 
	print(chr(mlist.index(m)+65)) #아스키 코드를 구해 문자열로 변환			
	
#97~122 : 소문자 a~z
#65~90 : 대문자 A~Z