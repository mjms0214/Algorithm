n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]


def dfs(node, count):
    global finish
    visited[node] = True
    if node == target2:
        finish = True
        print(count)
    for i in graph[node]:
        if not visited[i]:
            dfs(i,count+1)


finish = False
dfs(target1,0)
if not finish:
    print(-1)