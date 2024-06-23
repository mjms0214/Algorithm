# 전체 흰색 도화지에 대한 2차원 배열
white_paper = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())

for i in range(N):
    x, y = map(int, input().split())

    # 검은색 색종이에 대한 값 적용
    for j in range(x, x+10):
        for k in range(y, y+10):
            white_paper[j][k] += 1

zero_cnt = 0

# 검은색 영역이 아닌 부분 count
for i in range(100):
    zero_cnt += white_paper[i].count(0)

# 검은색 영역 넓이 구하기
cnt = (100*100) - zero_cnt
print(cnt)