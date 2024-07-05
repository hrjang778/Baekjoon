import sys
input = sys.stdin.readline
count = {}
N = int(input())
comparedCard = [*map(int,input().split())]
M = int(input())
compareCard = [*map(int,input().split())]
for i in comparedCard:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in compareCard:
    if count.get(i) == None:
        print(0, end = " ")
    else:
        print(count.get(i), end = " ")
# count[i] 보다는 count.get(i)를 사용하기 -> count[i]는 KeyError를 유발하기 때문
# 반면 count.get(i)는 값이 없으면 None 값을 리턴
# 또한 리스트 보다 딕셔너리가 속도가 빠르다
# 리스트 -> O(N)
# 딕셔너리 -> O(1)