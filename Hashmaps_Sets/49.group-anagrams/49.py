from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for word in strs:
            ls=[0]*26
            for char in word:
                ls[ord(char)-97]+=1
            ls=tuple(ls)
            if ls not in dict:
                dict[ls]=[word]
            else:
                dict[ls].append(word)

        return list(dict.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict =defaultdict(list)
        for word in strs:
            ls=[0]*26
            for char in word:
                ls[ord(char)-97]+=1
            ls=tuple(ls)
            dict[ls].append(word)

        return list(dict.values())

            