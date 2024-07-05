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


# 어떤 고수의 코드
# from itertools import tee
# from sys import stdin, stdout

# def pairwise(it):
#     a, b = tee(it)
#     next(b, None)
#     return zip(a, b)

# arr = sorted(stdin.buffer.read().split()[2:])
# arr = [a for a, b in pairwise(arr) if a == b]
# stdout.buffer.write(b'%d\n' % len(arr))
# stdout.buffer.write(b'\n'.join(arr))