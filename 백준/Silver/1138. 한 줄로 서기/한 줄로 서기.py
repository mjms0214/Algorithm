n = int(input())

arr = [0 for _ in range(n)]

tall_guys = list(map(int, input().split()))

for i in range(len(tall_guys)):
    temp = tall_guys[i]
    for j in range(n):
        if temp == 0 and arr[j] == 0:
            arr[j] = i+1
            break
        if arr[j] == 0:
            temp -= 1
            continue
            
print(' '.join(map(str, arr)))
