# leetcode solution link:https://leetcode.com/problems/jump-game/submissions/2171141973

def canJump(nums):
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1): 
            if (i + nums[i]) >= goal:  
                goal = i
        return  True if goal == 0 else False
    
print(canJump([1,6,4,2]))