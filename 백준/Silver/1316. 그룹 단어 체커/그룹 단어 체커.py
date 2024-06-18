N = int(input())
cnt = 0

for i in range(N):
    # 이전에 나온 문자 배열
    char_type = []
    str_list = list(input())

    group = True
    for j in range(len(str_list)):
        # 다음 문자가 연속 되지 않고 이후 문자 열에서 동일한 문자가 존재 하는 경우 그룹 단어가 아니다.
        if str_list[j] in str_list[j+2:] and str_list[j] != str_list[j+1]:
            group = False
            break

    if group:
        cnt += 1

print(cnt)