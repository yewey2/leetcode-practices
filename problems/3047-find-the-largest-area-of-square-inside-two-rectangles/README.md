# Find the Largest Area of Square Inside Two Rectangles (LeetCode 3047)

- Link: https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles
- Difficulty: Medium
- Started: 23:15
- Solved: 23:30

We need the largest square that fits in the intersection of at least two rectangles. This adds up to checking pairwise overlaps.

Approach: Brute-force every rectangle pair, compute their intersection width and height, take the smaller side as the square size, and track the best area. This runs in O(n^2) with O(1) extra space.

To improve: Research a subquadratic method (likely sweep line or coordinate compression over edges) to skip empty overlaps when n is large.
