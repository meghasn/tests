class TrieNode:
    def __init__(self):
        self.count=0
        self.children=[False for i in range(26)]
        
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for i in range(len(word)):
            c=word[i]
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')]=TrieNode()
            curr.count+=1
            curr=curr.children[ord(c)-ord('a')]
        
            
                
            
        

    def search(self, word: str) -> bool:
        curr=self.root
        for i in range(len(word)):
            c=word[i]
            if not curr.children[ord(c)-ord('a')]:
                return 0
            curr=curr.children[ord(c)-ord('a')]
        return curr.count
            
        
        

    def calc(self,word,prefix):
        curr=self.root
        for i in range(len(word)):
            c=word[i]
            self.insert(c)
        return self.search(prefix)
obj=Trie()
print(obj.calc(['abc','aab','bad','dab'],"ae"))