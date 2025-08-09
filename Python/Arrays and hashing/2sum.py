from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            if nums[0] + nums[1] != target:
                return []
            else:
                return [0, 1]
        n = len(nums) - 1
        count = 0
        for i in range(n):
            count += 1
            if (target - nums[i]) in nums[i + 1:]:
                new_nums = nums[i + 1:]
                return [i, new_nums.index(target - nums[i]) + count]

        return []
