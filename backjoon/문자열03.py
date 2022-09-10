# 10809 알파벳 찾기

# 97~122 : 알파벳 a 부터 z 까지

mlist = [-1 for i in range(26)] #크기 26 내용 -1

s = input()

for i in range(len(s)):
	for j in range(97,123):
		if s[i] == chr(j) and mlist[j-97] == -1:
			mlist[j-97] = i

for i in mlist:
	print(i,end = " ")






