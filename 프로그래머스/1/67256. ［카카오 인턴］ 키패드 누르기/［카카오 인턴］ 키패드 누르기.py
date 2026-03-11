# 번호 키 위치 사이의 이동거리 구하는 함수
def getDistance(start, end):
    # 키보드 배열에 대한 좌표 딕셔너리
    keypad = {1 : (0,0), 2 : (1,0), 3 : (2,0) 
             ,4 : (0,1), 5 : (1,1), 6 : (2,1)
             ,7 : (0,2), 8 : (1,2), 9 : (2,2)
             ,'*' : (0,3), 0 : (1,3), '#' : (2,3)}
    start_key = keypad[start]
    end_key = keypad[end]
    
    # 순서 상관 없이 구하기 위한 절대값 계산
    distance = abs(start_key[0] - end_key[0]) + abs(start_key[1] - end_key[1])
    return distance
    
    
def solution(numbers, hand):
    answer = ''
    # 처음 시작 위치
    last_right = '#'
    last_left = '*'
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            last_left = number
        elif number in (3, 6, 9):
            answer += 'R'
            last_right = number
        else:
            # 눌러야 하는 번호와 현재 왼손 엄지 위치 사이의 거리 계산
            left_distance = getDistance(last_left , number)
            # 눌러야 하는 번호와 현재 오른손 엄지 위치 사이의 거리 계산
            right_distance = getDistance(last_right , number)
            # 두 거리가 같다면
            if left_distance == right_distance:
                # 오른손잡이면 오른손 엄지
                if hand == 'right':
                    answer += 'R'
                    last_right = number
                # 왼손잡이면 왼손 엄지
                else:
                    answer += 'L'
                    last_left = number
            # 두 거리가 다르다면 가까운 손 이동
            # 왼손이 더 가까운 경우
            elif left_distance < right_distance:
                answer += 'L'
                last_left = number
            # 오른손이 더 가까운 경우
            else:
                answer += 'R'
                last_right = number
            
    print(answer)
    return answer