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
        current_node = self.root
        for i in range(0, len(word)):
            char = word[i]
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        node = self.root
        for i in range(0, len(prefix)):
            char = prefix[i]
            if char in node.children:
                node = node.children[char]
            else:
                return []

        return node


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

# Todo: case when inserting empty or None
