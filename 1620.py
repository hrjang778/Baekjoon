import sys
input = sys.stdin.readline
N,M = map(int,input().split())
poket = {}
poketIndex = {}
for i in range(N):
    name = input().strip()
    poket[name] = str(i+1)
    poketIndex[str(i+1)] = name

for i in range(M):
    ask = input().strip()
    if ask in poket:
        print(poket[ask])
    else:
        print(poketIndex[ask])