import sys
input = sys.stdin.readline
N,M = map(int,input().split())
unListen = [input().strip() for i in range(N)]
unLook = [input().strip() for i in range(N)]
duplication = []
for i in unListen:
    if i in unLook:
        duplication.append(i)