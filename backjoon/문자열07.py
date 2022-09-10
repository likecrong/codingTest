#2908 상수

import sys

mlist = sys.stdin.readline().split()

newMlist =[] #숫자를 뒤집어 저장하는 정수형 리스트
new = "" #해당 숫자를 뒤집은 문자열

for i in mlist:
	for j in range(2,-1,-1): # 2,1,0 순으로 내림차순
		new += i[j]
	newMlist.append(int(new)) #문자열을 정수형으로 리스트에 저장
	new = "" #이전 문자열 초기화
print(max(newMlist)) #가장 큰 값을 출력		