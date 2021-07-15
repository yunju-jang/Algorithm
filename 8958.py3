import sys
input = sys.stdin.readline
num = int(input())
sum = 0
cnt = 0
arr=[]
for i in range(num):
  lst = list(str(input()))
  for j in lst:
    cnt +=1
    if j == 'O':
      sum += cnt
    elif j == 'X':
      cnt = 0
  arr.append(sum)
  sum = 0
  cnt = 0

for i in arr:
  print(i)