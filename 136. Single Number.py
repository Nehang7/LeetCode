# leetcode solution :https://leetcode.com/problems/single-number/submissions/2172100684
class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        i = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                nums.pop(i - 1)
                i = 1
            else:
                return nums[i - 1]

        return nums[0]
