class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ls1=list(word1)
        ls2=list(word2)
        ls=[]


        small=min(len(ls1),len(ls2))
        for i in range(0,small):
            ls.append(ls1[i])
            ls.append(ls2[i])

        if (len(ls1)>len(ls2)):
            # for i in range(small,len(ls1)):
            #     string=string+ls1[i]
            ls.extend(ls1[small:])
        elif(len(ls1)<len(ls2)):
            ls.extend(ls2[small:])

           
        
        string=''.join(ls)
        return string 
        