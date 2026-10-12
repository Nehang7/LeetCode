# leetcod solution link :https://leetcode.com/problems/merge-sorted-array/submissions/2170199686


def merge(nums1, m, nums2, n):
    newnum1 = nums1[:m]
    newnum2 = nums2[:n]

    nums1[:] = sorted(newnum1 + newnum2)
    print(nums1)


merge(
    nums1=[1, 2, 3, 0, 0, 0],
    m=3,
    nums2=[2, 5, 6],
    n=3,
)
