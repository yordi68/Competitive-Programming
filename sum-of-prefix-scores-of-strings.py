class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        count = 0
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
            count += node.count

        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        count = 0
        for char in word:
            node = node.children[char]
            count += node.count

        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        length = len(words)
        res = [0]*length
        NewTrie = Trie()

        for word in words:
            NewTrie.insert(word)

        for idx in range(length):
            res[idx] = NewTrie.search(words[idx])
  
        return res