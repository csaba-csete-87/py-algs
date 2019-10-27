## Problem 4
To achieve single traversal, we are going to use three pointers: 
 - one for the 2s
 - one for the 0s 
 - one for the current index of the array iterator
At *each* iteration we are either going to increase the array iterator, or decrease the pointer of the 2s index or both, until the two pointers meet.
### Time Complexity
Since we have achieved single traversal, Time Complexity is O(n)
### Space Complexity
Space Complexity scales with number of items in the input list, so it will be O(n)