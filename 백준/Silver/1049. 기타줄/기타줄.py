n,m = map(int, input().split())

six_list = []
one_list = []

for i in range(m):
    a, b = map(int, input().split())
    six_list.append(a)
    one_list.append(b)

six = n // 6
one = n % 6
result1 = min(six_list)*six + min(one_list)*one
result2 = min(six_list)*(six+1)
result3 = min(one_list)*n
print(min(result1, result2, result3))