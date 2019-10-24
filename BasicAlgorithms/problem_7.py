# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, value):
        if value not in self.children:
            self.children[value] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        node = self.root
        for part in parts:
            node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, parts):
        node = self.root
        for part in parts:
            if part == "/":
                continue
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, error_handler):
        self.root_handler = root_handler
        self.error_handler = error_handler
        self.route_trie = RouteTrie()

    def add_handler(self, route, handler):
        parts = self.split_path(route)
        self.route_trie.insert(parts, handler)

    def lookup(self, route):
        if not route or route == "/":
            return self.root_handler
        parts = self.split_path(route)
        handler = self.route_trie.find(parts)
        if not handler:
            return self.error_handler
        return handler

    def split_path(self, route):
        parts = route.split("/")
        paths = []
        for i in range(1, len(parts)):
            if parts[i]:
                paths.append("/" + parts[i])
        return paths


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("Root", "404 - Page Not Found")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "About Page")  # add a route

# some lookups with the expected output
print(router.lookup(""))  # should print 'root handler'
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/////"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/contact"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/login"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/////"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
