# 종류별 개수 구하는 함수
def countCoin(C):
    # 거스름돈 종류 리스트
    coin_list = [25,10,5,1]
    # 종류별 개수 리스트
    coin_count = [0,0,0,0]

    i = 0
    while True:
        # 모든 종류에 대하여 계산이 끝났을 때
        if i == 4:
            break
        # 거스름돈 중 해당 종류로 거슬러 주어야 할 개수 계산
        coin_count[i] += C // coin_list[i]
        C %= coin_list[i]
        i += 1

    return coin_count

# 테스트 케이스 개수
T = int(input())

for i in range(T):
    # 거스름돈 금액
    C = int(input())
    coin_count = countCoin(C)

    # 출력 형식에 맞게 출력
    for i in coin_count:
        print(i, end = ' ')
