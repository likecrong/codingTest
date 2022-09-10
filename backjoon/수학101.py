# 1712 손익분기점
import sys

mlist = [int(x) for x in sys.stdin.readline().split()]

# a == mlist[0] 
# b == mlist[1]
# c == mlist[2]

# x = a/(b-c)
if mlist[1] != mlist[2]: #분모가 0 방지 
	result = int (mlist[0]/(mlist[2] - mlist[1]))+1
	# x에 1을 더하면 손익분기점을 넘는 최소 판매 대수가 result가 된다.
	if result > 0: #팔긴 팔아야 되니까 0대보다는 커야 된다.
		print(result)
	else:
		print(-1)
else:
	print(-1)