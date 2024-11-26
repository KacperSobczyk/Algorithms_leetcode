class Solution(object):
    """
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter
    in pattern and a non-empty word in s. Specifically:

    * Each letter in pattern maps to exactly one unique word in s.
    * Each unique word in s maps to exactly one letter in pattern.
    * No two letters map to the same word, and no two words map to the same letter.

    Constraints:

    * 1 <= pattern.length <= 300
    * pattern contains only lower-case English letters.
    * 1 <= s.length <= 3000
    * s contains only lowercase English letters and spaces ' '.
    * s does not contain any leading or trailing spaces.
    * All the words in s are separated by a single space.
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if self.__set_initial_conditions(pattern,s):
            D = {}
            word_list = s.split()
            if len(pattern) != len(word_list):
                return False
            for i in range(len(word_list)):
                if pattern[i] not in D and word_list[i] not in D.values():
                    D[pattern[i]] = word_list[i]
                else:
                    if (pattern[i] not in D and word_list[i] in D.values() or
                        D[pattern[i]] != word_list[i]):
                        return False
            else:
                return True
        else:
            raise ValueError("Solution doesn't meet the initial conditions")

    def __set_initial_conditions(self, pattern: str, s: str) -> bool:
        return(len(pattern) >= 1 and
               len(pattern) <= 300 and
               pattern.isalpha() and pattern.islower() and 
               len(s) >= 1 and len(s) <= 3000 and
               s.replace(" ", "").isalpha() and s.islower() and
               not s.startswith(" ") and not s.endswith(" "))   

if __name__ == "__main__":
    obj = Solution()
    print(obj.wordPattern("aaaa", "dog cat cat dog"))    