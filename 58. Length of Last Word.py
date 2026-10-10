##Leetcode soltion :https://leetcode.com/problems/length-of-last-word/submissions/2168045354


class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        return len(a[-1])
