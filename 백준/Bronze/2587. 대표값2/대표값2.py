nums = []

for _ in range(5):
    num = input()
    nums.append(int(num))

nums.sort()
# 평균
avg = sum(nums)/5
print(int(avg))

# 중앙값
print(nums[2])