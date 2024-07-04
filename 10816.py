import sys
input = sys.stdin.readline
N = int(input())
comparedCard = list(map(int,input().split()))
M = int(input())
compareCard = list(map(int,input().split()))
for i in compareCard:
    print(comparedCard.count(i),end=' ')
# 딕셔너리 이용해 볼것