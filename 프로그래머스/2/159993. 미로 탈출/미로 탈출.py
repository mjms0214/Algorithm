from collections import deque

def bfs(maps, start, grid, n, m, target):
    queue = deque()
    queue.append(start)
    
    distance = 0
    finalx = -1
    finaly = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and maps[nx][ny] in ('S', 'O', 'L', 'E'):
                grid[nx][ny] = grid[x][y] + 1
                if target == maps[nx][ny]:
                    finalx = nx
                    finaly = ny
                    return finalx, finaly
                else:
                    queue.append((nx, ny))

    return finalx, finaly

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    sx = 0
    sy = 0
    lx = 0
    ly = 0
    
    grid = [[0] * m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] in ('S', 'O', 'L', 'E'):
                if maps[i][j] == 'S':
                    sx = i
                    sy = j
                else :
                    grid[i][j] = 1
            else:
                grid[i][j] = 0
    
    # S -> L 까지 최소 거리
    slx, sly = bfs(maps, (sx, sy), grid, n, m, 'L')
    if slx == -1 or sly == -1:
        return -1
    distanceSL = grid[slx][sly]
    
    # 그리드 초기화 : 같은 곳을 다시 지날 수 있기 때문
    grid = [[0] * m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] in ('S', 'O', 'L', 'E'):
                if maps[i][j] == 'L':
                    lx = i
                    ly = j
                else: 
                    grid[i][j] = 1
            else:
                grid[i][j] = 0
    
    
                
    # L -> E 까지 최소 거리
    lex, ley = bfs(maps, (lx, ly), grid, n, m, 'E')
    if lex == -1 or ley == -1:
        return -1
    distanceLE = grid[lex][ley]

    answer = distanceSL + distanceLE
    
    return answer