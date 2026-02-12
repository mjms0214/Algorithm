def solution(board, moves):
    answer = 0

    # 바구니
    basket = []
    
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                # 가장 위에 있는 인형 뽑고 그 자리 0으로 채우기
                pick = board[j][moves[i]-1]
                board[j][moves[i]-1] = 0
                
                if len(basket) == 0:
                    basket.append(pick)
                else:
                    # basket 제일 위에 담긴 인형과 비교
                    # 같으면 인형 개수 count + basket에서 제거
                    # 다르면 인형 추가
                    if basket[-1] == pick:
                        basket.pop()
                        answer += 2
                    else:
                        basket.append(pick)
                break
    
    return answer