import sys
input = sys.stdin.readline

def selfNum(n):
  return n+sum(map(int,str(n)))

pre = list()
for i in range(1,10000):
  pre.append(selfNum(i))

for i in range(1,10001):
  if pre.count(i) == 0:
    print(i)
