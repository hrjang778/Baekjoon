import sys
input = sys.stdin.readline
N,M = map(int,input().split())
unListen = set([input().strip() for i in range(N)])
unLook = set([input().strip() for i in range(M)])
duplication = []
for i in unListen:
    if i in unLook:
        duplication.append(i)
duplication.sort()
print(len(duplication))
for i in duplication:
    print(i)