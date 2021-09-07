import sys
input = sys.stdin.readline

def cont(n):
  a = list()
  count = 0
  for i in range(1,n+1):
    a=list((map(int,str(i))))
    if i < 100 :
      count +=1
    elif a[1]-a[0] == a[2]-a[1]:
      count +=1
  return count

num = int(input())
print(cont(num))