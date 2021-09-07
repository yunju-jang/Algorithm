import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
sum = a*b*c
lst = list(map(int,str(sum)))
for i in range(0,10):
  print(lst.count(i))