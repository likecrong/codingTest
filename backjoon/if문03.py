# 10817

numlist = [int(x) for x in input().split()]
#1. input함수를 통해 한 줄을 입력받는다.
#2. split함수를 통해 문자열을 분리한다.
#3. 문자열을 정수형으로 바꾼 뒤 numlist에 저장한다.
numlist = sorted(numlist, reverse = True)

print(numlist[1])