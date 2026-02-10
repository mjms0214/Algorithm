def solution(n, lost, reserve):
    answer = 0
    # 1. lost, reserve에 모두 속한 경우
    set_lost = set(lost)
    set_reserve = set(reserve)
    set_union = set_lost.intersection(set_reserve)

    if len(set_union) != 0 :
        #lost, reserve에서 제거
        lost = [x for x in lost if x not in set_union]
        reserve = [x for x in reserve if x not in set_union]

    # 2. lost에 없는 학생
    answer += (n - len(lost))
    
    lost.sort()
    reserve.sort()
    
    # 3. lost에 있지만 앞뒤 숫자가 reserve 포함되는 경우
    for lost_student in lost:
        # 여벌 체육복이 있는 학생이 존재하지 않으면, break
        if len(reserve) == 0 :
            break

        if lost_student - 1 in reserve:
            reserve.pop(reserve.index(lost_student-1))
            answer += 1
        elif lost_student + 1 in reserve:
            reserve.pop(reserve.index(lost_student+1))
            answer += 1
    
    return answer