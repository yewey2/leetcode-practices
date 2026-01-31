# Minimum Operations to Make the Integer Zero (LeetCode 2749)

- Link: https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
- Difficulty: Medium

## Description

You are given two integers num1 and num2. In one operation, you can choose integer i in the range [0, 60] and subtract 2^i + num2 from num1. Return the minimum number of operations needed to make num1 equal to 0. If impossible, return -1.

## Attempt details

### Attempt 1
- Date: 2026-01-31
- Started: 8:00 PM
- Stopped: 8:12 PM (worked on initial approach)
- Continued: 10:19 PM - 10:32 PM (completed independently without solution)
- Total Time: 25 minutes

Approach: Using algebraic manipulation, recognize that `num1 - num2*k = sum of 2^i`. The key insight is that after k operations, we subtract `2^i + num2` k times, leaving us with `num1 - num2*k`. This value must be representable as a sum of powers of 2 (which all non-negative integers are), and the number of set bits (bit_count) in this value represents the minimum 2^i values needed. For a valid k, we need `k >= bit_count(num1 - num2*k)`. We brute force all k from 0 to 60.

Time Complexity: O(60) = O(1)
Space Complexity: O(1)

To improve: The solution works but the `binary` helper function is incomplete/unused. The built-in `bit_count()` method handles bit counting efficiently.
