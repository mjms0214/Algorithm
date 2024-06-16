# 계산식
expression = input()

# 계산 결과
result = 0

num_list = expression.split("-")

# minus 가 없는 경우
if len(num_list) == 1:
    num_list = map(int, expression.split("+"))
    result = sum(num_list)
else:
    # minus 나오기 전까진 더하고 그 이후 숫자는 모두 뺀다.
    for i in range(len(num_list)):
        if i == 0:
            result = sum(map(int, num_list[i].split("+")))
        else:
            result -= sum(map(int, num_list[i].split("+")))

print(result)
