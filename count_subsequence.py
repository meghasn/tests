class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hmap={}
        buckets=[[] for i in range(len(s))]
        count=0
        for i in range(len(s)):
            if s[i] not in hmap.keys():
                hmap[s[i]]=[]
            hmap[s[i]].append(i)
        for i in words:
            c=i[0]
            if c in hmap.keys():
                idx=hmap[c]
                buckets[idx[0]].append(i)
                
        
        for i in range(len(buckets)):
            
            li=buckets[i]
            
                # ch=li[0][0]
                # if ch in hmap.keys():
            
            del hmap[s[i]][0]

            for j in li:
                if len(j)==1:
                    count+=1
                else:
                    if j[1] in hmap.keys():
                        idx=hmap[j[1]]
                        if idx != []:
                            
                            buckets[idx[0]].append(j[1:])
            
        return count
                    
                    
                
                
