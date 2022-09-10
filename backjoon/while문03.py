# 15552

import sys

num = int(input())
ans = []
for i in range(num):
	list = sys.stdin.readline().split()
	ans.append(int(list[0]) + int(list[1]))

for i in ans:
	print(i)