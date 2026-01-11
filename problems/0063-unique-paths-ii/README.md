# Unique Paths II (LeetCode 63)

- Link: https://leetcode.com/problems/unique-paths-ii
- Difficulty: Medium
- Started: 12:05am
- Solved: 12:34am

This folder contains the submitted solution and a tiny runner for local checks.

Approach: Top-left recursion with memoization keyed by subgrid slices. On each step, try moving down or right if the next cell isn’t an obstacle, and sum the counts. Caches intermediate subproblems by stringifying the subgrid state.


TO OPTIMIZE:
To change the approach from `[1:]` into a DP pointer, so that we don't use so much time of re-creating the grid.