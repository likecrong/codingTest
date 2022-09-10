# 2884

userinput = input()

time = userinput.split(' ')
ans = int(time[1]) - 45

if ans >= 0 :
    print (time[0] + ' ' + str(ans))
else :
    h = int(time[0]) - 1
    m = int(time[1]) + 15
    
    if h < 0 :
        h = 24 + h
    print (str(h) + ' ' + str(m))