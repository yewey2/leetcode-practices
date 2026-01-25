# Minimize Maximum Pair Sum in Array (LeetCode 1877)

- Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
- Difficulty: Medium

## Description

The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array `nums` of even length `n`, pair up the elements of `nums` into `n / 2` pairs such that:

- Each element of `nums` is in exactly one pair, and
- The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.

## Attempt details

### Attempt #1
- Date: 2026-01-24
- Started: 8.06
- Solved: 12.12
- Duration: 6 minutes

Approach: Sort the array and pair the smallest with the largest, second smallest with second largest, etc. This pairing minimizes the worst-case pair sum due to balancing extremes. Track the maximum of these sums.

Complexity: Sorting `O(n log n)`, pairing pass `O(n)`, space `O(1)` beyond sort.

To improve: None needed; two-pointer variant avoids indexing.
