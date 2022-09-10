# 1110 더하기 사이클

def change(num):
	if len(num) == 1:
		n1 = "0"
		n2 = num
	else :
		n1 = num[0]
		n2 = num[1]
	return n1, n2

def sum(x1, x2):
	result = int(x1) + int(x2)
	return result

if __name__ == "__main__":
	
	x = input()
	oldx1, oldx2 = change(x) # 정답
	a1 = oldx1
	a2 = oldx2
	
	count = 1 		
	while True:
		r = sum(a1 , a2)
		a1 = a2
		
		n1, n2 = change(str(r))
		a2 = n2

		if oldx1 == a1 and oldx2 == a2:
			print(count)
			break

		count += 1