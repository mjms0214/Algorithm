n = int(input())
m = int(input())

ingredient = list(map(int, input().split()))
ingredient.sort()

cnt = 0
for i in range(n):
    if m-ingredient[i] in ingredient:
        cnt += 1


print(int(cnt/2))