class Solution:
    def __init__(self):
        self.visited=None
        self.hmap={}
    def countComponents(self, n, edges):
        self.visited=[False for i in range(n)]
        
        count=0
        for i in edges:
            if i[0] not in self.hmap.keys():
                self.hmap[i[0]]=[]
            self.hmap[i[0]].append(i[1])
        print(self.hmap)
        for i in self.hmap.keys():
            if self.visited[i]==False:
                self.dfs(self.hmap[i],i)
                count+=1
        print(count,"x")
        return count
    
    def dfs(self,li,index):
        self.visited[index]=True
        print(self.visited)
        for i in range(len(li)):
            print(li[i])
            if self.visited[li[i]]==False:
                if li[i] in self.hmap.keys():
                    print(self.hmap[li[i]])
                    self.dfs(self.hmap[li[i]],li[i])


        





obj=Solution()
print(obj.countComponents(5,[[0,1],[1,2],[3,4]]))
