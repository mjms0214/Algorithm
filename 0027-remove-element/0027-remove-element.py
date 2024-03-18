class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        idx = 0
        for i  in range(len(nums)):
            if val == nums[i]:
                idx = i
                break
        
        if idx == 0 and val != nums[0]:
            return len(nums)

        for j in range(idx+1, len(nums)):
            if val == nums[idx]:
                if val == nums[j]:
                    continue
                tmp = nums[idx]
                nums[idx] = nums[j]
                nums[j] = tmp
                idx += 1

        return idx

