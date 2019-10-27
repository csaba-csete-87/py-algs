## Problem 3
Having an array of sorted values from highest to lowest would make this problem really simple.
Since we cannot use any python provided methods, we can just modify the mergesort algorithm, because it has the same time complexity no matter what.
### Time Complexity
Sorting the values takes O(n log(n)) and building the values takes O(n), which equals to O(n log(n))
### Space Complexity
Space Complexity scales with number of items in the input list, so it will be O(n)