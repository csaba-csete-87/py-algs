## Problem 7
Let's analyze the solution by classes:

### RouteTrieNode
The `insert` method just creates a new node, both time and space complexities are O(1)

### RouteTrie
The `insert` method has a time complexity of O(n) where n is the number of route parts we are inserting into the trie, and because the `insert` method of the node runs in O(1). Space complexity is also O(n), where n is the number of parts.
The `find` method just accesses the already inserted parts, so it's fast running, time complexity is O(n), where n equals to the number of parts the route has, space complexity is O(1), it does not require any extra space.

### Router
The `split_path` method runs in O(n), where n is the length of the route, space complexity is also O(n), where n is the length of the route.

The `add_handler` method runs in O(n), where n would be the length of the route. As established before, splitting up the route into parts takes O(n) and then inserting the parts into the trie also O(n), for the total of O(n). Space complexity is O(n), where n is the number of parts inserted into the trie.

Finally, the `lookup` method, according to the before mentioned time complexities split_path - O(n), find - O(n), results also in O(n), where n is the length of the route.
Space complexity is O(1), it does not need any extra space to do its work.

