from sys import stdin
input = stdin.readline
N,M = map(int,input().split())
A = set([*map(int,input().split())])
B = set([*map(int,input().split())])

def subList(A,B):
    subResult = [i for i in A if i not in B]
    return subResult
print(len(subList(A,B)) + len(subList(B,A)))