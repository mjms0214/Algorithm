# 단어 입력
word = input()

# 전체 소문자로 변경
word = word.lower()

# 중복 제거
word_type = list(set(word))
cnt = []

# 개수 세기
for i in word_type:
    cnt.append(word.count(i))

# 최대 값
max_count = max(cnt)
# 최대 값이 여러개면
if cnt.count(max_count) > 1:
    print('?')
else:
    max_char_idx = cnt.index(max_count)
    print(word_type[max_char_idx].upper())