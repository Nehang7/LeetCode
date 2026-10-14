# leetcode solution link:https://leetcode.com/problems/valid-anagram/submissions/2172115901

s = "anagram"
t = "nagaram"

sorted_s = sorted(s)
sorted_t = sorted(t)
print(sorted_s)
print(sorted_t)

if sorted_s == sorted_t:
    print("True")
else:
    print("false")
