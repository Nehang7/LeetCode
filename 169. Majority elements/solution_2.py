class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        freq = 0

        for i in range(0, len(nums)):
            if nums[i] == nums[i - 1]:
                freq += 1
            else:
                freq = 1

            if freq > len(nums) // 2:
                return nums[i]