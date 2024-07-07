import sys
def binary_search(cards, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if cards[mid] == target:
            print("1", end=" ")
            return
        elif cards[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("0", end=" ")



n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

left = 0
right = len(cards) - 1

for i in range(m):
    binary_search(cards, left, right, check[i])
