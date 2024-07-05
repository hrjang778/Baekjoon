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

# in 함수는 set함수를 사용하게 될때 해시테이블을 이용하므로 O(1) 시간 복잡도를 가진다
# in 함수는 list에서 O(N)을 가짐