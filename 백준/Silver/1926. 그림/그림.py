from collections import deque


# BFS 메서드 정의
def bfs(graph, i, j, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([(i, j)])
    # 현재 노드를 방문 처리
    visited[i][j] = True

    # 동서남북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    size = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        tmp_i, tmp_j = queue.popleft()
        size += 1
        # 해당 원소와 연결된, 아직 방문 하지 않은 원소들을 큐에 삽입
        for k in range(4):
            if tmp_i + dx[k] < 0 or tmp_i + dx[k] >= len(graph) or tmp_j + dy[k] < 0 or tmp_j + dy[k] >= len(graph[0]):
                continue

            if not visited[tmp_i + dx[k]][tmp_j + dy[k]] and graph[tmp_i + dx[k]][tmp_j + dy[k]] == 1:
                queue.append((tmp_i + dx[k], tmp_j + dy[k]))
                visited[tmp_i + dx[k]][tmp_j + dy[k]] = True
    return size


n, m = map(int, input().split(' '))

# 색칠된 부분 입력
paper = []
for i in range(n):
    paper.append(list(map(int, input().split(' '))))

# 방문 처리를 위한 배열
visited = [[False for j in range(m)] for i in range(n)]

cnt = 0
maxSize = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            size = bfs(paper, i, j, visited)
            if size > maxSize:
                maxSize = size
            cnt += 1

print(cnt)
print(maxSize)
