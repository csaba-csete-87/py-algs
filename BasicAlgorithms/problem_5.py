class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char not in self.children:
            node = TrieNode()
            self.children[char] = node

    def suffixes(self):
        result = []
        for key in self.children:
            node = self.children[key]
            suffixes = node.suffixes()
            if node.is_word:
                result.append(key)
            for s in suffixes:
                result.append(key + s)
        return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        current_node = self.root
        for i in range(0, len(word)):
            char = word[i]
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        if not prefix:
            return TrieNode()
        prefix = str(prefix)
        prefix = prefix.lstrip()
        node = self.root
        for i in range(0, len(prefix)):
            char = prefix[i]
            if char in node.children:
                node = node.children[char]
            else:
                return TrieNode()

        return node


print("Test Case 1")

my_trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun",
    "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    my_trie.insert(word)

print(my_trie.find("f").suffixes())
# Should print ['actory', 'un', 'unction']
print(my_trie.find("p").suffixes())
# Should print []
print(my_trie.find(3).suffixes())
# Should print []

print("Test Case 2")

trie2 = Trie()
wordList = [
    "area", "astral", "anonymous", "ace",
    "back", "bear", "broke", "big",
    "can", "call", "cell", "controversy"
]
for word in wordList:
    trie2.insert(word)
trie2.insert("")
trie2.insert(None)
print(trie2.find("a").suffixes())
# Should print ['rea', 'stral', 'nonymous', "ce"]
print(trie2.find("   c").suffixes())
# Should print ['an', 'all', 'ell', "ontroversy"]
print(my_trie.find("d").suffixes())
# Should print []
print(my_trie.find("").suffixes())
# Should print []
print(my_trie.find(None).suffixes())
# Should print []

print("Test Case 3")

empty_trie = Trie()
wordList = []

print(empty_trie.find("a").suffixes())
# Should print []
print(my_trie.find("").suffixes())
# Should print []
print(my_trie.find(None).suffixes())
# Should print []
