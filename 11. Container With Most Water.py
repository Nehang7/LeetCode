# LeetCode solution Link: https://leetcode.com/problems/container-with-most-water/submissions/2170169583
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maxWater = 0
lp = 0
rp = len(h) - 1

while lp < rp:
    w = rp - lp
    ht = min(h[lp], h[rp])
    currentWater = w * ht
    maxWater = max(maxWater, currentWater)

    if h[lp] < h[rp]:
        lp += 1
    else:
        rp -= 1

print(maxWater)
