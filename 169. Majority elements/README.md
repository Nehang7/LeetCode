# 169. Majority Element

## Problem Statement

Given an integer array `nums`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times, where `n` is the length of the array. The problem guarantees that a majority element exists.

**LeetCode:** [169. Majority Element](https://leetcode.com/problems/majority-element/)
[My Submission](https://leetcode.com/problems/majority-element/submissions/2180409511)
[My Submission](https://leetcode.com/problems/majority-element/submissions/2180401173)

**Difficulty:** Easy

## Example 1

**Input:** `nums = [3, 2, 3]`

**Output:** `3`

## Example 2

**Input:** `nums = [2, 2, 1, 1, 1, 2, 2]`

**Output:** `2`

## Approach 1: Boyer–Moore Voting Algorithm

### Idea

Maintain a candidate and a counter while traversing the array. When the counter is zero, choose the current element as the candidate. Increase the counter when the current element matches the candidate; otherwise, decrease it. Since a majority element appears more than half the time, it remains the final candidate.

### Implementation

See `solution1.py`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Auxiliary Space Complexity:** `O(1)`

## Approach 2: Sorting and Counting

### Idea

Sort the array so that equal elements become consecutive. Traverse the sorted array, count consecutive occurrences, and return the element as soon as its frequency exceeds `n // 2`.

### Implementation

See `solution2.py`.

### Complexity Analysis

- **Time Complexity:** `O(n log n)` due to sorting
- **Auxiliary Space Complexity:** Depends on Python's sorting implementation
- **Note:** Sorting modifies the original list.

## Approach Comparison

| Criteria | Boyer–Moore Voting | Sorting and Counting |
|---|---|---|
| Time Complexity | `O(n)` | `O(n log n)` |
| Auxiliary Space | `O(1)` | Depends on sorting implementation |
| Modifies Original List | No | Yes |
| Meets the Follow-up | Yes | No |

## Selected Approach

The **Boyer–Moore Voting Algorithm** is selected as the primary solution because it achieves `O(n)` time complexity and `O(1)` auxiliary space, satisfying the follow-up requirement.

## Edge Cases

| Scenario | Input | Expected Output |
|---|---|---|
| Standard example | `[3, 2, 3]` | `3` |
| Majority element appears at the end | `[1, 2, 3, 3, 3]` | `3` |
| Majority element appears at the beginning | `[1, 1, 1, 2, 3]` | `1` |
| All elements are the same | `[4, 4, 4, 4]` | `4` |
| Single element | `[7]` | `7` |

## Folder Structure

```text
169_majority_element/
├── README.md
├── solution1.py
└── solution2.py
```
