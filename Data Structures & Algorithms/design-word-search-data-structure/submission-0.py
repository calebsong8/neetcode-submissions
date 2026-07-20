class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    # think this is also a trie with the unique thing ebing the '.'
    # account for the periods:
    # once period is hit check every word until it appears
    # while loop from index to index
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.isEndOfWord
        
        return dfs(0, self.root)
