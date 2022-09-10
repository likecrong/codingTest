def solve(a):
	count = 0
	for i in range(1,a+1): #1~a번 반복
		if i < 100:
			count += 1
		else : #100 부터 검사
			charnum = str(i)
			gap = int(charnum[0]) - int(charnum[1])
			if (int(charnum[1]) - int(charnum[2])) == gap :
				count += 1
	print(count)

if __name__ == "__main__":
	x = int(input())
	solve(x)