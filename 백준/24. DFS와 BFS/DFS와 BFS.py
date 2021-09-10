import sys
from collections import deque
#DFS
def dfs(graph, num, visited):
  #방문한 노드 체크해주기
  visited[num] = [True]
  print(num, end=" ")

  #스택의 최상단 노드에 방문안한 인접한 노드 있는지 계속 검사
  for i in graph[num]:
    if visited[i] == False:
      visited[i] == [True]
      dfs(graph, i, visited)

#BFS
def bfs(graph, start, visited):
  #방문한 노드 체크해주기
  visited[start] = [True]

  #방문한 노드 큐에 넣기
  queue = deque([start])

  while queue:
    v = queue.popleft()
    print(v, end=" ")

    for i in graph[v]:
      if visited[i] == False:
        visited[i] = [True]
        queue.append(i)

input = sys.stdin.readline

n, l, s = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]

for i in range(l):
  x, y = map(int, input().split())
  graph[x][y] = y
  graph[y][x] = x

visitedDFS = [False] * (n+1)
visitedDFS[0] = [True]

visitedBFS = [False] * (n+1)
visitedBFS[0] = [True]

dfs(graph, s, visitedDFS)
print("")
bfs(graph, s, visitedBFS)