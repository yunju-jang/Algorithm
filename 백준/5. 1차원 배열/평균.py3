import sys
input = sys.stdin.readline
num = int(input())
arr = list(map(int, input().split()))
m = max(arr)
sum = 0
for i in arr:
  tmp = i/m*100
  sum += tmp

print(sum/num)