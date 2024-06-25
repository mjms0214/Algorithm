import sys
from collections import deque


def dfs(vertex):
    stack = []
    stack.append(vertex)
    vis[vertex] = True
    print(vertex, end=' ')
    while stack:
        now_vertex = stack[-1]
        can_go = False
        for next_vertex in range(1, n + 1):
            if adj_matrix[now_vertex][next_vertex] == 1:
                if vis[next_vertex] == False:
                    vis[next_vertex] = True
                    can_go = True
                    print(next_vertex, end=' ')
                    stack.append(next_vertex)
                    break
        if not can_go:
            stack.pop()


def bfs(vertex):
    q = deque()
    q.append(vertex)
    vis[vertex] = True
    while q:
        now_vertex = q.popleft()
        print(now_vertex, end=' ')
        for next_vertex in range(1, n + 1):
            if adj_matrix[now_vertex][next_vertex] == 1:
                if vis[next_vertex] == False:
                    vis[next_vertex] = True
                    q.append(next_vertex)


n, m, v = map(int, sys.stdin.readline().split())
adj_matrix = [[0] * (n + 1) for _ in range(n+1)]
vis = [False] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj_matrix[a][b] = 1
    adj_matrix[b][a] = 1
dfs(v)
print()
for i in range(n + 1):
    vis[i] = False
bfs(v)