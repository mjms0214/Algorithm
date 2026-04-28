from collections import deque

def bfs(place, start):
    q = deque()
    visited = [[False]*5 for _ in range(5)]
    
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x, y, dist = q.popleft()
        
        # 거리 2까지만 탐색
        if dist > 2:
            continue
        
        # 자기 자신 제외하고 P 만나면 실패
        if dist > 0 and place[x][y] == 'P':
            return False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and place[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))
    
    return True

def solution(places):
    answer = []
    
    for place in places:
        valid = True
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, (i,j)):
                        valid = False
                        break
            if not valid:
                break
        
        answer.append(1 if valid else 0)
    
    return answer
