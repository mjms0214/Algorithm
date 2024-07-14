def binary_search(l, start, end, target):
    mid = (start + end) // 2

    while start <= end:
        mid = (start + end) // 2
        if l[mid] < target:
            if mid+1 <= end and l[mid+1] < target:
                start = mid + 1
            else:
                return mid
        else:
            end = mid - 1

    return mid - 1


t = int(input())

cnt_list = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort()

    total = 0
    for i in range(n):
        cnt = binary_search(b, 0, m-1, a[i])
        total += cnt+1
    cnt_list.append(total)

for j in cnt_list:
    print(j)