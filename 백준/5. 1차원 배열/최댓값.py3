import sys
input = sys.stdin.readline
a=list()
for i in range(1,10):
  ap = int(input())
  a.append(ap)

print(max(a))
print(a.index(max(a))+1)