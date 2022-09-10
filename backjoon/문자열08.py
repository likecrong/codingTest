#5622 다이얼

x = [x for x in input()]
#65~90
count = 0
for i in x:
	result = int((ord(i)-65) / 3)
	if result <= 4: 
		count += result+3
	else:
		if ord(i) >= 80 and ord(i) <=83:
			count += 8
		elif ord(i) <= 86:
			count += 9
		else:
			count += 10		

print(count)
