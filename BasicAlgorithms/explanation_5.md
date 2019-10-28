## Problem 5
Let's analyze the solution by classes:

### TrieNode
The `insert` method just creates a new node, both time and space complexities are O(1)
In the `suffixes` method, we would traverse down the trie, each node having n elements and for worst case scenarion a depth of m, where m is the longest word, so time complexity will result O(n log(n)), whereas space complexity scales with the depth of the trie, so O(n)

### Trie
The `insert` method has a time complexity of O(n) where n is the length of the word we are inserting into the trie, and because the `insert` method of the node runs in O(1). Space complexity is also O(n), where n is the length of the word.
The `find` method just accesses the children of the trie, so it's fast running,
time complexity is O(n), where n is the length of the `prefix`, space complexity is O(1), it does not use any extra space.