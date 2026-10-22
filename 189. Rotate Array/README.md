# 189. Rotate Array

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

The rotation must modify the original array in-place.

**LeetCode:** [189. Rotate Array][My Submission](https://leetcode.com/problems/rotate-array/submissions/2176161303/)

**Difficulty:** Medium

## Example 1

**Input:**
```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

**Output:**
```python
[5, 6, 7, 1, 2, 3, 4]
```

## Example 2

**Input:**
```python
nums = [-1, -100, 3, 99]
k = 2
```

**Output:**
```python
[3, 99, -1, -100]
```

## Approach 1: Three Reversals

### Idea

Rotate the array using three reversal operations:

1. Reverse the entire array.
2. Reverse the first `k` elements.
3. Reverse the remaining elements.

Before performing the reversals, calculate `k % len(nums)` to handle rotations greater than or equal to the array length.

### Complexity Analysis

- **Time Complexity:** O(n)
- **Auxiliary Space Complexity:** O(1)


## Approach 2: Slicing and Concatenation

### Idea

Divide the array into two parts:

- The last `k` elements.
- The remaining elements before them.

Concatenate the two parts in reverse order and assign the result to `nums[:]` to replace the contents of the original list.

### Implementation

See `solution2.py`.

### Complexity Analysis

- **Time Complexity:** O(n)
- **Auxiliary Space Complexity:** O(n)


## Approach Comparison

| Criteria | Three Reversals | Slicing |
|---|---|---|
| Time Complexity | O(n) | O(n) |
| Auxiliary Space | O(1) | O(n) |
| Modifies Original List | Yes | Yes, using `nums[:]` |
| Meets O(1) Extra-Space Follow-up | Yes | No |

## Selected Approach

The **three-reversal approach** is selected as the primary solution because it achieves O(n) time complexity and O(1) auxiliary space.


## Edge Cases

Test the following scenarios:

| Scenario | Input | Expected Output |
|---|---|---|
| Standard rotation | `[1, 2, 3, 4, 5]`, `k = 2` | `[4, 5, 1, 2, 3]` |
| No rotation | `[1, 2, 3]`, `k = 0` | `[1, 2, 3]` |
| Rotation equals length | `[1, 2, 3]`, `k = 3` | `[1, 2, 3]` |
| Rotation exceeds length | `[1, 2, 3]`, `k = 5` | `[2, 3, 1]` |
| Single element | `[5]`, `k = 4` | `[5]` |

## Folder Structure

```text
189_rotate_array/
├── README.md
├── solution1.py
└── solution2.py
```
