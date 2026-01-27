def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    
    # 0을 제외한 내 로또
    new_lottos = [x for x in lottos if x != 0]
    
    # 0을 제외한 내 로또 중에서 당첨 로또 안에 존재하는 번호의 개수
    win_nums_set = set(win_nums)
    include_lottos_cnt = sum(1 for x in new_lottos if x in win_nums_set)
    
    best_match = include_lottos_cnt + zero_cnt
    worst_match = include_lottos_cnt
    
    best = min(7 - best_match, 6)
    worst = min(7 - worst_match, 6)
    
    answer = [best, worst]
    return answer