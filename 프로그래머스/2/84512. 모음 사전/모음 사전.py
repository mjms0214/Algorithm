def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    cnt = 0
    answer = 0

    def dfs(current_word):
        nonlocal cnt, answer
        if current_word == word:
            answer = cnt
            return True # 단어를 찾았다는 신호
        
        if len(current_word) == 5:
            return False

        for v in vowels:
            cnt += 1
            if dfs(current_word + v): # 찾았으면 즉시 중단
                return True
        return False

    dfs("")
    return answer