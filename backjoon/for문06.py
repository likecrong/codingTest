# 2439

x = int(input())

for i in range(x):
	for j in range(x-i-1):
		print(" ",end = "")
	for k in range(i+1):
		print("*",end = "")
	print()