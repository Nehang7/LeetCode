##Leetcode Soltion link:
##https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/2167137516

class Solution(object):
    def removeDuplicates(self, nums):
		i = 1
		while i <len(nums):
			if nums[i] == nums[i - 1]:
				nums.pop(i)
			else:
				i += 1
		return len(nums)
        