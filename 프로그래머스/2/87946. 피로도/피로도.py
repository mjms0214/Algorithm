def dfs(k, dungeons, visited):
    # 기본적으로 현재까지 탐험한 수는 0에서 시작 (더 갈 곳이 없을 때를 대비)
    max_cnt = 0
    
    for i in range(len(dungeons)):
        # 아직 방문 안 했고, 최소 필요 피로도 만족 시
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True  # 방문 처리
            
            # (중요) 다음 단계로 넘어가서 받은 결과에 '나 자신(1)'을 더함
            current_path_cnt = 1 + dfs(k - dungeons[i][1], dungeons, visited)
            
            # 여러 갈래 길 중에서 가장 큰 값을 선택
            max_cnt = max(max_cnt, current_path_cnt)
            
            visited[i] = False # 백트래킹
            
    return max_cnt

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited)