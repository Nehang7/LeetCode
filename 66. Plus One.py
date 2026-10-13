# leetcode solution link:https://leetcode.com/problems/plus-one/submissions/2171171092
def plusOne(digits):
        
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits


digits=[1,9,9]
print(plusOne(digits))