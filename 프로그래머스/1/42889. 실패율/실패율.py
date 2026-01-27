# i번 스테이지 실패율 = (stages 중 i인 값의 개수) / (stages 중 i보다 크거나 같은 값의 개수)
def solution(N, stages):
    fail_rate = [0] * N
    
    for i in range(0, N):
        # stages 중 i인 값의 개수
        player_cnt = stages.count(i+1)
        # stages 중 i보다 크거나 같은 값의 개수
        total_player_cnt = sum(1 for stage in stages if stage >= i+1)
        
        if total_player_cnt == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = player_cnt / total_player_cnt

    answer = [i + 1 for i in sorted(range(len(fail_rate)), key=lambda i: fail_rate[i], reverse=True)]

    return answer