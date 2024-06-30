import sys
print(type(2))
N,M = map(int,sys.stdin.readline().split())
poket = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    poket[name] = str(i+1)
for i in range(M):
    ask = sys.stdin.readline().strip()
    try:
        print(poket[ask])
    except:
        for key, value in poket.items():
            if value == ask:
                print(key)