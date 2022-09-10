#15596 정수 N개의 합

num = 0

def solve(a):
	global num
	for i in a:
		num += i
	return num

if __name__ == '__main__' :
	list = [3,3,4,4,5]
	print(solve(list))
