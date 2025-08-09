from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_new = {}
        for i in nums:
            if i in dict_new:
                dict_new[i] += 1
            else:
                dict_new[i] = 1
        for j in dict_new:
            if dict_new[j] > 1:
                return True

        return False
