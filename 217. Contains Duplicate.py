# leetcode solution link :https://leetcode.com/problems/contains-duplicate/submissions/2168083868/


class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
