## Problem 2
If the array wasn't rotated it would have been a simple binary search problem.
But in this case we have to split the array in two parts, right where the largest and smallest values meet. This way we can keep just simply do the binary search in one of the arrays.
### Time Complexity
Searching for the location where we will split the array will take O(log(n)) time, and finding a value in a sorted array also takes O(log(n)) time.
Time complexity is log(n)
### Space Complexity
Space Complexity scales with the size of the input, so it will be O(n)