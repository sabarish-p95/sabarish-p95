class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = []
        t_list = []
        for i in s:
            s_list.append(i)
        for j in t:
            t_list.append(j)

        s_list.sort()
        t_list.sort()
        if s_list == t_list:
            return True
        return False
