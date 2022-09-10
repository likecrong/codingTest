#2941 크로아티아 알파벳

x = input()
num = len(x)

count = 0
mlist = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in mlist:
	count += x.count(i)
print(num - count)