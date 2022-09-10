# 1316 그룹 단어 체커

T = int(input())

flag = 0 #그룹 단어 체커
	#0: 그룹 단어, 1: 비 그룹 단어
count = 0 #그룹 단어의 수

mlist = [] # 입력된 문자열 리스트
arrange = [] #연속된 문자를 제거한 문자열 리스트

for i in range(T):
	mlist.append(input())

for i in mlist:
	for j in range(len(i)):
		if j == 0: #첫번째 글자
			arrange.append(i[j])
		else :	
			if not i[j-1] == i[j]: #현재문자와 이전문자가 같지 않을 때 (연속된 문자가 아닐 때)
				arrange.append(i[j])
	for k in arrange:
		if arrange.count(k) >= 2: #편집된 문자열 안에 중복된 원소가 존재할 때
			flag = 1
			break #하나라도 중복된 원소가 있으면 무조건 그룹단어가 될 수 없다.
	if flag == 0: #그룹단어 일 때
 		count += 1

	#arrange는 mlist의 한 원소를 편집하는 데 사용
	#계산 과정이 끝나면 변수와 리스트 초기화 (재사용 하기 때문)
	flag = 0		
	arrange.clear()

print(count)