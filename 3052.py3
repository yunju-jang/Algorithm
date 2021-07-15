import sys
input = sys.stdin.readline
lst= []
for i in range(10):
  ap = int(input())
  lst.append(int(ap%42))
cnt = 0
for i in range(42):
  if lst.count(i)>0:
    cnt+=1

print(cnt)
