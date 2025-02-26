class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] #first ele is set as prefix
        for str in strs[1:]:   #exclude first ele of list
            while str.startswith(prefix) != True:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix