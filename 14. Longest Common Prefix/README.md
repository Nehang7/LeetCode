# 14. Longest Common Prefix

## Problem Statement

Given an array of strings, return the longest prefix shared by every string. If no common prefix exists, return an empty string (`""`).

**LeetCode:** [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) 
[My Solution](https://leetcode.com/problems/longest-common-prefix/submissions/2183890936)
[My Solution](https://leetcode.com/problems/longest-common-prefix/submissions/2183895626)

**Difficulty:** Easy

### Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- Each non-empty string contains only lowercase English letters.

## Examples

**Example 1**

```text
Input:  strs = ["flower", "flow", "flight"]
Output: "fl"
```

**Example 2**

```text
Input:  strs = ["dog", "racecar", "car"]
Output: ""
```

There is no common prefix among the input strings.

## Approach 1: `os.path.commonprefix`

### Idea

Use Python's `os.path.commonprefix` to find the starting characters shared by all the strings. If no starting characters match, the answer is `""`.

### Implementation

See [`solution_1.py`](solution_1.py).

### Complexity Analysis

Let `S` mean the number of characters in all the strings combined.

- **Time: `O(S)`** - The work grows with the total number of input characters. More characters to compare means more work.
- **Extra space: `O(m)`** - The answer can contain up to `m` characters, where `m` is the length of the shortest string.

## Approach 2: Shrink the Candidate Prefix

### Idea

Treat the first string as a guess for the answer. Check whether each other string starts with that guess. If not, remove one character from the end and check again. Stop when every string matches or the guess is empty.

### Implementation

See [`solution_2.py`](solution_2.py).

### Complexity Analysis

Let `n` be the number of strings and `p` be the length of the first string.

- **Time: `O(n * p^2)` in the worst case** - For each string, the guess might be shortened many times. Each check can look at many characters, so the work can grow roughly like `p * p` for each string. With more strings, that work repeats.
- **Extra space: `O(p)`** - The guess is at most as long as the first string.

## Approach Comparison

| Criteria | `os.path.commonprefix` | Shrink the Candidate Prefix |
|---|---|---|
| Main technique | Standard-library character-prefix comparison | Repeated `startswith` checks |
| Time | `O(S)` - grows with all input characters | `O(n * p^2)` worst case - may recheck a shrinking guess |
| Extra space | `O(m)` for the answer | `O(p)` for the guess |

## Edge Cases

| Scenario | Input | Expected Output |
|---|---|---|
| No common prefix | `["dog", "racecar", "car"]` | `""` |
| One string is a prefix of another | `["interview", "inter"]` | `"inter"` |
| A string is empty | `["", "abc"]` | `""` |
| All strings are identical | `["same", "same"]` | `"same"` |
| Single string | `["alone"]` | `"alone"` |

## Folder Structure

```text
14. Longest Common Prefix/
├── README.md
├── solution_1.py
└── solution_2.py
```
