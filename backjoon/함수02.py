# 4673 셀프 넘버
def solve():
	mlist = []
	x = 0 # 현재 수
	
	num = 0 #생성자를 가진 수

	#0부터 9999까지 채운 mlist
	for i in range(10000):
		mlist.append(i)
	
	while x < 10000:
		num = 0
		num += x
		charx = str(x)
		
		for i in charx:
			num += int(i)

		if num in mlist: #리스트에 생성자를 가진 수를 가지면
    			mlist.remove(num) # 제거
		x += 1
	for i in mlist: #생성자를 가지지 않은 수만 남음
		print(i)

if __name__ == '__main__':
	solve()