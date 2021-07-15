import sys
input = sys.stdin.readline
num = int(input())
a=list(map(int,input().split()))
print(min(a), end=" ")
print(max(a))