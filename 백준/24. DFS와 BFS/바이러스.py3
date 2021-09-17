import sys

def dfs(graph, v, visited):
  visited[v] = [True]

  for i in graph[v]:
    if visited[i] == False:
      visited[i] = [True]
      dfs(graph, i, visited)
  return visited.count([True])-2

input = sys.stdin.readline

num = int(input())
line = int(input())
graph = [[False]*(num+1) for i in range(num+1)]

for i in range(line):
  x, y = map(int, input().split())
  graph[x][y] = y
  graph[y][x] = x
visited = [False] * (num+1)
print(dfs(graph, 1, visited))