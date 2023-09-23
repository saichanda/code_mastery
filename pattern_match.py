"""
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list = [*pattern]
        s_list = s.split(' ')
        if len(p_list) != len(s_list):
            return False
        match = {}
        for i in range(len(p_list)):
            if not p_list[i] in match:
                if s_list[i] in match.values():
                    return False
                match[p_list[i]] = s_list[i]
            elif match[p_list[i]] != s_list[i]:
                return False
        
        return True


#TODO: To write main function to call the wordPatter method of Solution class.
