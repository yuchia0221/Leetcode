class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.max_length = 0
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        l = 0
        for w in word:
            if w not in node.links:
                node.links[w] = TrieNode()
            node = node.links[w]
            l += 1

        self.max_length = max(self.max_length, l)
        node.end = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_length:
            return False

        def helper(index: int, node: TrieNode):
            for index in range(index, len(word)):
                c = word[index]
                if c == ".":
                    for child in node.links.values():
                        if helper(index+1, child):
                            return True
                    return False
                else:
                    if c not in node.links:
                        return False
                    node = node.links[c]

            return node.end
        return helper(0, self.root)
