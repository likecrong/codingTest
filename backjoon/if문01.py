# 2753

userinput = int(input())

if userinput % 4 == 0:
    if userinput % 100 == 0:        
        if userinput % 400 == 0:
            print(1)
        else :
            print(0)
    else:
        print(1)
else :
    print(0)